@echo off
REM Smart Recommender System - Windows Batch Launcher
REM Double-click this file to launch the app

echo.
echo ========================================================
echo.
echo           SMART RECOMMENDER SYSTEM
echo.
echo      Books - Courses - Movies Recommender
echo.
echo ========================================================
echo.

REM Check if app.py exists
if not exist "app.py" (
    echo ERROR: app.py not found!
    echo Please run this script from the ai_project3 directory.
    echo.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8 or higher from python.org
    echo.
    pause
    exit /b 1
)

echo Python found!
echo.

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo WARNING: Streamlit not installed.
    echo.
    set /p install="Would you like to install dependencies now? (y/n): "
    
    if /i "%install%"=="y" (
        echo.
        echo Installing dependencies...
        pip install -r requirements.txt
        
        if errorlevel 1 (
            echo.
            echo ERROR: Failed to install dependencies.
            echo Please run manually: pip install -r requirements.txt
            echo.
            pause
            exit /b 1
        )
        
        echo.
        echo Dependencies installed successfully!
    ) else (
        echo.
        echo Please install dependencies first:
        echo   pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
)

echo.
echo ========================================================
echo   Launching Smart Recommender System...
echo ========================================================
echo.
echo The app will open in your default browser
echo URL: http://localhost:8501
echo.
echo Press Ctrl+C in this window to stop the app
echo ========================================================
echo.

REM Launch Streamlit
streamlit run app.py

echo.
echo App stopped. Thanks for using Smart Recommender System!
pause
