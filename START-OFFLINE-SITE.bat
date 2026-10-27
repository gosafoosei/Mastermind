@echo off
setlocal
where py >nul 2>nul
if %errorlevel%==0 (
  start "Mastermind Offline Site" /D "%~dp0" cmd /k "py -3 -m http.server 8000 --bind 127.0.0.1"
) else (
  where python >nul 2>nul
  if errorlevel 1 (
    echo Python 3 is required. Install it from python.org, then run this file again.
    pause
    exit /b 1
  )
  start "Mastermind Offline Site" /D "%~dp0" cmd /k "python -m http.server 8000 --bind 127.0.0.1"
)
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000/index.html"
echo Keep the server console open while using the site. Close it to stop the server.
endlocal
