import cv2
import json
import asyncio
import base64
import torch
import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from ultralytics import YOLO
from insightface.app import FaceAnalysis

app = FastAPI()

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"--- Model Loading on: {device} ---")

# 1. โหลด YOLO สำหรับนับคน (Person Detection)
model_yolo = YOLO("yolo26n.pt").to(device)

# 2. โหลด InsightFace สำหรับเจาะลึกใบหน้า
print("--- Loading InsightFace (buffalo_l) ---")
face_app = FaceAnalysis(name='buffalo_l')
face_app.prepare(ctx_id=0 if device == 'cuda' else -1, det_size=(640, 640))

@app.websocket("/ws/analytics")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("--- Client Connected ---")
    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    try:
        while cap.isOpened():
            success, frame = cap.read()
            if not success: break

            # --- Step 1: รัน YOLO นับคนรวม ---
            results = model_yolo(frame, verbose=False, device=device)
            count = (results[0].boxes.cls == 0).sum().item()
            annotated_frame = results[0].plot()

            # --- Step 2: รัน InsightFace ดึงอายุและเพศ ---
            faces = face_app.get(frame)
            for face in faces:
                bbox = face.bbox.astype(int)
                x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]
                
                age = int(face.age)
                gender = 'Male' if face.sex == 'M' else 'Female'
                
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{gender}, {age}"
                cv2.putText(annotated_frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # --- Step 3: ส่งข้อมูลขึ้นเว็บ ---
            annotated_frame = cv2.resize(annotated_frame, (640, 480))
            _, buffer = cv2.imencode('.jpg', annotated_frame)
            image_base64 = base64.b64encode(buffer).decode('utf-8')

            data = {
                "count": int(count),
                "status": "Crowded" if count > 5 else "Normal",
                "image": image_base64
            }

            try:
                await websocket.send_text(json.dumps(data))
            except Exception:
                break
            
            await asyncio.sleep(0.03)

    except WebSocketDisconnect:
        print("--- Client Web Page Closed ---")
    finally:
        cap.release()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)