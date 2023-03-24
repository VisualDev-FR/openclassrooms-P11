@echo off
call ".\env\Scripts\activate.bat"
set FLASK_APP=server.py
flask run
