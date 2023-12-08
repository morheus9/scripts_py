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
Poetry:
```
# https://python-poetry.org/docs/#installing-with-the-official-installer
poetry self update

poetry init
poetry shell
poetry install
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
poetry env info
```
Mini conda:
```
# https://docs.conda.io/projects/miniconda/en/latest/
conda update -n base conda

conda install -n base conda-libmamba-solver
conda config --set solver libmamba
conda config --show-sources

conda create -n CONDA python=3.11
conda create -n CONDA -f requirements.yml
conda env list
conda env remove -n CONDA
conda install -y pandas
conda list
conda remove -y pandas
conda env export -f requirements.yml
conda clean -a
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
