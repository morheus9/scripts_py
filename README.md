# My scripts.
```
#!/usr/bin/env python
chmod +x myfile.py
```
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
sudo apt install python3.12 python3.12-venv
python3.12 -V
```
Poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
poetry self update

poetry shell or poetry init
poetry add fastapi
poetry add ruff -G dev
poetry remove fastapi
poetry env list
poetry env use /usr/bin/python3.11 or poetry env use python3.11
poetry env remove -n envname
poetry env remove --all
poetry export --without-hashes --format=requirements.txt > requirements.txt
poetry show --tree
```
Micromamba:
```
# https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
micromamba self-update
./bin/micromamba shell init -s bash -p ~/micromamba

micromamba create -n BASED -conda-forge
micromamba create -n name -f mamba.yml
micromamba activate BASED
micromamba deactivate
micromamba install fastapi
micromamba list
micromamba remove fastapi
micromamba env list
micromamba env export > mamba.yml
micromamba env remove -n name
micromamba clean --all (delete cache)
```
