@echo off
echo ====================================================
echo   Launching News Analytics Platform (v2)...
echo ====================================================
echo.

REM Check if the environment exists
call conda info --envs | findstr "crisis-dashboard" >nul
if errorlevel 1 (
    echo [INFO] Environment 'crisis-dashboard' not found. Creating it now...
    call conda create -n crisis-dashboard python=3.9 streamlit pandas altair numpy -y
    call conda activate crisis-dashboard
    pip install python-dotenv nltk "openai==0.28.0"
    echo [INFO] Environment created successfully!
)

REM Activate Environment
echo Activating 'crisis-dashboard' environment...
call conda activate crisis-dashboard

REM Check dependencies (simple check)
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Streamlit not found. Installing core dependencies...
    pip install streamlit pandas altair numpy nltk python-dotenv "openai==0.28.0"
)

REM Run the App
echo Starting Streamlit...
streamlit run Home2.py --server.headless true

echo.
echo Application closed.
pause
