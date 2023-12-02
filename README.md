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
Micro conda:
```
conda create -n CONDA python=3.11
conda env list
conda env remove -n CONDA
conda install pandas
conda list
conda remove pandas
conda clean -a (delete caches)
```
Micro mamba:
```
# https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
micromamba self-update
./bin/micromamba shell init -s bash -p ~/micromamba

micromamba create -n MAMBA python=3.1
micromamba create -n MAMBA -f mamba.yml
micromamba env list
micromamba env remove -n MAMBA
micromamba activate MAMBA
micromamba deactivate
micromamba install pandas
micromamba list
micromamba remove pandas
micromamba env export > mamba.yml
micromamba clean -a (delete caches)
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
poetry cache list
poetry cache clear PyPI --all
```
