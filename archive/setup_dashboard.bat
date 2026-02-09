@echo off
REM Setup script for News Analytics Dashboard
REM This script helps you set up the Streamlit dashboard

echo ========================================
echo News Analytics Dashboard Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo [1/5] Python found
echo.

REM Check if .env file exists
if not exist .env (
    echo [2/5] Creating .env file from template...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file and add your OpenAI API key
    echo           Open .env and replace 'your_openai_key_here' with your actual key
    echo.
) else (
    echo [2/5] .env file already exists
    echo.
)

REM Install dependencies
echo [3/5] Installing dashboard dependencies...
pip install -r requirements-dashboard.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Download NLTK data
echo [4/5] Downloading NLTK data...
python -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('stopwords', quiet=True); nltk.download('punkt_tab', quiet=True)"
if errorlevel 1 (
    echo WARNING: Failed to download NLTK data
    echo You may need to download it manually
)
echo.

REM Check if data file exists
echo [5/5] Checking for data file...
if exist data\processed\all_clean_df.csv (
    echo Data file found: data\processed\all_clean_df.csv
) else (
    echo.
    echo WARNING: Data file not found at data\processed\all_clean_df.csv
    echo Please place your processed CSV file in this location
    echo Or update the DATA_PATH in your .env file
)
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file and add your OpenAI API key
echo 2. Ensure your data CSV is at: data\processed\all_clean_df.csv
echo 3. Run the dashboard: streamlit run app.py
echo.
echo For more information, see README_DASHBOARD.md
echo.
pause
