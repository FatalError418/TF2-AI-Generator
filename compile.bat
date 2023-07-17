@echo off
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pyinstaller --onefile --name app --icon=tf2_icon.ico --distpath compile --workpath compile gui.py weapongenerator.py
move app.spec compile
