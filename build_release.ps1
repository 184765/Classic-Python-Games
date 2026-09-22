Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

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

Write-Host "Installing dependencies..." -ForegroundColor Cyan
& $pythonCommand -m pip install --upgrade pip
& $pythonCommand -m pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Error "Dependency installation failed."
    exit $LASTEXITCODE
}

Write-Host "Building the executable..." -ForegroundColor Cyan
& $pythonCommand build_exe.py

if ($LASTEXITCODE -ne 0) {
    Write-Error "Executable build failed."
    exit $LASTEXITCODE
}

$sourceExe = Join-Path $repoRoot 'dist\ClassicPythonGames.exe'
$releaseFolder = Join-Path $repoRoot 'release\ClassicPythonGames'
$finalZip = Join-Path $repoRoot 'release\ClassicPythonGames-Windows.zip'

if (-not (Test-Path $sourceExe)) {
    Write-Error "Executable not found at $sourceExe"
    exit 1
}

if (-not (Test-Path $releaseFolder)) {
    New-Item -ItemType Directory -Path $releaseFolder -Force | Out-Null
}

Copy-Item $sourceExe $releaseFolder -Force

$readmePath = Join-Path $releaseFolder 'README.txt'
if (-not (Test-Path $readmePath)) {
    @'
Classic Python Games
===================

This is the Windows release for the Classic Python Games project.

How to run:
1. Extract this ZIP file.
2. Double-click ClassicPythonGames.exe to start the game.
3. If Windows blocks the app, click "More info" and then "Run anyway".

Included files:
- ClassicPythonGames.exe

Notes:
- This is a standalone executable.
- No installation is required.
'@ | Set-Content -Path $readmePath -Encoding UTF8
}

if (Test-Path $finalZip) {
    Remove-Item $finalZip -Force
}

Compress-Archive -Path (Join-Path $releaseFolder '*') -DestinationPath $finalZip -Force

Write-Host "Release package created successfully." -ForegroundColor Green
Write-Host "Download this file:" -ForegroundColor Green
Write-Host $finalZip -ForegroundColor Green
Write-Host "Inside the ZIP, you will find:" -ForegroundColor Cyan
Write-Host "- ClassicPythonGames.exe" -ForegroundColor Cyan
Write-Host "- README.txt" -ForegroundColor Cyan
