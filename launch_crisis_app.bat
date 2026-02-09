@echo off
echo ====================================================
echo   Launching Crisis Monitoring Dashboard...
echo ====================================================
echo.

REM Check if the environment exists
call conda info --envs | findstr "crisis-dashboard" >nul
if errorlevel 1 (
    echo [ERROR] Environment 'crisis-dashboard' not found!
    echo Please run the setup steps in README_SETUP.md first.
    echo.
    pause
    exit /b
)

REM Activate Environment
echo Activating 'crisis-dashboard' environment...
call conda activate crisis-dashboard

REM Check dependencies (simple check)
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Streamlit not found. Attempting to install core dependencies...
    pip install streamlit pandas altair numpy nltk python-dotenv "openai==0.28.0"
)

REM Run the App
echo Starting Streamlit...
streamlit run Home.py

echo.
echo Application closed.
pause
