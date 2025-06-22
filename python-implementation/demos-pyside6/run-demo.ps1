# Fine Use Design System - PySide6 Demo Installation & Launch Script
# This script installs dependencies and runs the demo in one command

Write-Host "🚀 Fine Use Design System - PySide6 Demo" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Gray

# Check if we're in the right directory
$currentDir = Split-Path -Leaf (Get-Location)
if ($currentDir -ne "demos-pyside6") {
    Write-Host "❌ Please run this script from the demos-pyside6 directory" -ForegroundColor Red
    Write-Host "Expected location: ...\Fine-Use-Design-System\python-implementation\demos-pyside6" -ForegroundColor Yellow
    exit 1
}

Write-Host "📁 Current directory: $(Get-Location)" -ForegroundColor Green
Write-Host ""

# Install PySide6
Write-Host "📦 Installing PySide6..." -ForegroundColor Yellow
Write-Host "   (This may take 1-2 minutes - PySide6 is ~200MB)" -ForegroundColor Gray

try {
    # Try multiple installation methods
    $installCommands = @(
        "pip install PySide6",
        "python -m pip install PySide6", 
        "py -m pip install PySide6"
    )
    
    $installed = $false
    foreach ($cmd in $installCommands) {
        Write-Host "   Trying: $cmd" -ForegroundColor Gray
        $result = Invoke-Expression "$cmd 2>&1"
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ PySide6 installed successfully!" -ForegroundColor Green
            $installed = $true
            break
        }
    }
    
    if (-not $installed) {
        Write-Host "❌ Failed to install PySide6 with all methods" -ForegroundColor Red
        Write-Host "Please try manually: pip install PySide6" -ForegroundColor Yellow
        exit 1
    }
}
catch {
    Write-Host "❌ Error during installation: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🎯 Features you'll see:" -ForegroundColor Cyan
Write-Host "   • Perfect button alignment (no pixel drift)" -ForegroundColor White
Write-Host "   • 10 professional themes" -ForegroundColor White
Write-Host "   • Real-time metric updates" -ForegroundColor White
Write-Host "   • Mathematical layout precision" -ForegroundColor White
Write-Host ""

# Launch the demo
Write-Host "🚀 Launching Fine Use Demo..." -ForegroundColor Yellow

try {
    # Try different Python commands
    $pythonCommands = @("python", "py", "python3")
    
    $launched = $false
    foreach ($pythonCmd in $pythonCommands) {
        try {
            Write-Host "   Trying: $pythonCmd fine_use_pyside6_demo.py" -ForegroundColor Gray
            
            # Check if Python command exists
            $null = Get-Command $pythonCmd -ErrorAction Stop
            
            # Launch the demo
            & $pythonCmd "fine_use_pyside6_demo.py"
            $launched = $true
            break
        }
        catch {
            continue
        }
    }
    
    if (-not $launched) {
        Write-Host "❌ Could not find Python interpreter" -ForegroundColor Red
        Write-Host "Please ensure Python is installed and in your PATH" -ForegroundColor Yellow
        exit 1
    }
}
catch {
    Write-Host "❌ Error launching demo: $_" -ForegroundColor Red
    Write-Host "Try running manually: python fine_use_pyside6_demo.py" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "✅ Fine Use Demo completed successfully!" -ForegroundColor Green
Write-Host "🎉 Perfect button alignment achieved!" -ForegroundColor Cyan
