Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

Write-Host "Classic Python Games - Windows build script" -ForegroundColor Cyan
Write-Host "Working folder: $repoRoot" -ForegroundColor DarkCyan

$pythonCommand = $null

if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCommand = 'py'
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCommand = 'python'
}
else {
    Write-Error "Python was not found on PATH. Install Python 3.10+ and try again."
    exit 1
}

Write-Host "Using Python command: $pythonCommand" -ForegroundColor DarkCyan

& $pythonCommand -m pip install --upgrade pip
& $pythonCommand -m pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Error "Dependency installation failed."
    exit $LASTEXITCODE
}

Write-Host "Building the Windows executable..." -ForegroundColor Yellow
& $pythonCommand build_exe.py

if ($LASTEXITCODE -ne 0) {
    Write-Error "Executable build failed."
    exit $LASTEXITCODE
}

$exePath = Join-Path $repoRoot 'dist\ClassicPythonGames.exe'
$zipDirectory = Join-Path $repoRoot 'release'
$zipPath = Join-Path $zipDirectory 'ClassicPythonGames-Windows.zip'

if (Test-Path $exePath) {
    if (-not (Test-Path $zipDirectory)) {
        New-Item -ItemType Directory -Path $zipDirectory | Out-Null
    }

    if (Test-Path $zipPath) {
        Remove-Item $zipPath -Force
    }

    Compress-Archive -Path $exePath -DestinationPath $zipPath -Force

    Write-Host "SUCCESS: Windows executable created at:" -ForegroundColor Green
    Write-Host $exePath -ForegroundColor Green
    Write-Host "" -ForegroundColor Green
    Write-Host "DOWNLOAD THIS FILE:" -ForegroundColor Green
    Write-Host $zipPath -ForegroundColor Green
    Write-Host "" -ForegroundColor Green
    Write-Host "What to download:" -ForegroundColor Cyan
    Write-Host "- The EXE is the actual game file: ClassicPythonGames.exe" -ForegroundColor Cyan
    Write-Host "- The ZIP is just a packaged download file for convenience." -ForegroundColor Cyan
}
else {
    Write-Host "Build completed, but the executable was not found at the expected location:" -ForegroundColor Yellow
    Write-Host $exePath -ForegroundColor Yellow
    Write-Host "Check the dist folder manually." -ForegroundColor Yellow
}
