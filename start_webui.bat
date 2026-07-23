@echo off
cd /d %~dp0
call .venv\Scripts\activate.bat
start http://localhost:8080
python -m api.main
pause
