@echo off
echo ==========================================
echo   AI Dashboard Setup - Production Ready
echo   (YOLO + InsightFace)
echo ==========================================

echo [1/4] Creating Virtual Environment...
python -m venv venv

echo [2/4] Updating pip...
call venv\Scripts\python.exe -m pip install --upgrade pip

echo [3/4] Installing PyTorch with CUDA Support...
call venv\Scripts\pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

echo [4/4] Installing Core Libraries from requirements.txt...
call venv\Scripts\pip install -r requirements.txt

echo ==========================================
echo   MASTER DEPLOYMENT COMPLETE!
echo   To start the API and Dashboard, type: 
echo   python app.py
echo ==========================================
pause