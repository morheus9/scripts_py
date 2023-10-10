# My scripts.
For pyinstaller compilation to .bin use:
```
pip install pyinstaller
pyinstaller --onefile main.py
```
For nuitka:
```
sudo apt install patchelf
pip install nuitka
nuitka3 --onefile main.py
```
For installing python use:
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv
python3.11 -V
```
venv:
```
python3.11 -m venv name
pip freeze > requirements.txt 
pip3 install -r requirements.txt
```
script set
```
#!/usr/bin/env python
chmod +x myfile.py
```
