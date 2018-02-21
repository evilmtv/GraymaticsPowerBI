# GraymaticsPowerBI

## Set-up

### Download Anaconda
- Get latest anaconda from https://www.anaconda.com/download/
```
Version used: Anaconda 5.1 (Python 3.6 version)
OS used: Windows 10
```

### Set up Environment Variables
- Right-click `This PC`
- Click `Advanced System Settings`
- Click `Environment Variables`
- Under System Variables -> Path -> Click `Edit`
- Enable 'python':  
    Click `New` -> Click `Browse` -> Browse to C, ProgramData, Anaconda3 -> Click `OK`
- Enable 'conda':  
    Click `New` -> Click `Browse` -> Browse to C, ProgramData, Anaconda3, Scripts -> Click `OK`

### Update
Run command prompt as adminstrator
```bash
python -m pip install -U pip
python -m pip install --upgrade pip setuptools wheel
conda update -n base conda
conda update anaconda
conda update --all
```

### Install heatmappy and dependencies
Ensure command prompt in adminstrator
```bash
conda install matplotlib
conda install -c conda-forge moviepy  # If giving decorator dependency conflict, do: conda uninstall decorator
conda install numpy
conda install -c conda-forge pyside2
python -m pip uninstall Pillow
python -m pip install -U Pillow
python -m pip install -U imageio
python -m pip install -U --no-dependencies heatmappy
```

### Readings
- https://github.com/LumenResearch/heatmappy
- https://pypi.python.org/pypi/heatmappy
- https://stackoverflow.com/questions/12759761/python-pip-force-install-ignoring-dependencies
- https://stackoverflow.com/questions/39060669/python-matplotlib-install-issue-on-windows-7-for-freetype-png-packages/39060865
- https://github.com/python-pillow/Pillow/issues/2945
