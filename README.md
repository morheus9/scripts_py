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
Micromamba:
```
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
micromamba self-update

micromamba create -n name
micromamba install fastapi
micromamba list
micromamba remove fastapi
micromamba env list
micromamba env remove -n name
micromamba clean --all (delete packages)
```
Poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
poetry self update

poetry shell or poetry init
poetry add fastapi
poetry remove fastapi
poetry env list
poetry env remove --all
poetry export --without-hashes --format=requirements.txt > requirements.txt
poetry show --tree
```
