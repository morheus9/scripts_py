# My scripts.
For nuitka or pyinstaller compilation to .bin use:
```
pip install pyinstaller
pyinstaller --onefile main.py
```
and
```
sudo apt install patchelf
pip install nuitka
nuitka3 --onefile main.py
```

For python use:

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11-dev python3.11-venv
python3.11 -V
```
