@echo off
call ".\env\Scripts\activate.bat"
set FLASK_APP=app/server.py
flask run
