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
Poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
poetry self update

poetry shell or poetry init
poetry add fastapi
poetry remove fastapi
poetry env list
poetry env remove -n envname
poetry env remove --all
poetry export --without-hashes --format=requirements.txt > requirements.txt
poetry show --tree
```
