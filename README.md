# My scripts.
```
#!/usr/bin/env python
chmod +x myfile.py
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
# https://docs.conda.io/projects/miniconda/en/latest/
conda update -n base conda

conda install -n base conda-libmamba-solver
conda config --set solver libmamba
conda config --show-sources

conda create -n CONDA python=3.11
conda env list
conda env remove -n CONDA
conda install pandas
conda list
conda remove pandas
conda clean -a
```
Micro mamba:
```
# https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html
micromamba self-update

micromamba create -n MAMBA python=3.11
micromamba create -n MAMBA -f mamba.yml
micromamba env list
micromamba env remove -n MAMBA
micromamba activate MAMBA
micromamba deactivate
micromamba install pandas
micromamba list
micromamba remove pandas
micromamba env export > mamba.yml
micromamba clean -a
```
Poetry:
```
# https://python-poetry.org/docs/#installing-with-the-official-installer
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
