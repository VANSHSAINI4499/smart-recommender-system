# Smart Recommender System - Windows Launch Script
# Double-click this file to launch the app

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                                        ║" -ForegroundColor Cyan
Write-Host "║        🎯 SMART RECOMMENDER SYSTEM 🎯                 ║" -ForegroundColor Cyan
Write-Host "║                                                        ║" -ForegroundColor Cyan
Write-Host "║     Books 📚 | Courses 🎓 | Movies 🎬                 ║" -ForegroundColor Cyan
Write-Host "║                                                        ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check if app.py exists
if (-Not (Test-Path "app.py")) {
    Write-Host "❌ Error: app.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from the ai_project3 directory." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found!" -ForegroundColor Red
    Write-Host "Please install Python 3.8 or higher from python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if Streamlit is installed
$streamlitInstalled = python -c "import streamlit" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "⚠️  Streamlit not found!" -ForegroundColor Yellow
    $install = Read-Host "Would you like to install dependencies now? (y/n)"
    
    if ($install -eq "y" -or $install -eq "Y") {
        Write-Host ""
        Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
        pip install -r requirements.txt
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Dependencies installed successfully!" -ForegroundColor Green
        } else {
            Write-Host "❌ Failed to install dependencies." -ForegroundColor Red
            Write-Host "Please run manually: pip install -r requirements.txt" -ForegroundColor Yellow
            Read-Host "Press Enter to exit"
            exit 1
        }
    } else {
        Write-Host "Please install dependencies first: pip install -r requirements.txt" -ForegroundColor Yellow
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Check for CSV files
Write-Host ""
$csvFiles = @("books.csv", "courses.csv", "movies.csv")
$missingFiles = @()

foreach ($file in $csvFiles) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        Write-Host "✓ $file found ($size bytes)" -ForegroundColor Green
    } else {
        Write-Host "⚠ $file not found" -ForegroundColor Yellow
        $missingFiles += $file
    }
}

if ($missingFiles.Count -gt 0) {
    Write-Host ""
    Write-Host "⚠️  Some CSV files are missing." -ForegroundColor Yellow
    Write-Host "You can upload them via the app's sidebar once it launches." -ForegroundColor Cyan
    Write-Host ""
    $continue = Read-Host "Continue anyway? (y/n)"
    
    if ($continue -ne "y" -and $continue -ne "Y") {
        Write-Host "Please add CSV files and run again." -ForegroundColor Yellow
        Read-Host "Press Enter to exit"
        exit 0
    }
}

# Launch the app
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "🚀 Launching Smart Recommender System..." -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "📍 The app will open in your default browser" -ForegroundColor White
Write-Host "🌐 URL: http://localhost:8501" -ForegroundColor White
Write-Host "⏸️  Press Ctrl+C in this window to stop the app" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""

# Run Streamlit
try {
    streamlit run app.py
} catch {
    Write-Host ""
    Write-Host "❌ Error launching Streamlit." -ForegroundColor Red
    Write-Host "Try running manually: streamlit run app.py" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "👋 App stopped. Thanks for using Smart Recommender System!" -ForegroundColor Green
Read-Host "Press Enter to exit"
