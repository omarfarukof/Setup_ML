# setup-ml

This is a python script to create Machine Learning Projects (Template).

## Dependencies
- `python`
- `rye`

## Setup
- Download the repository
- add `setup- ml.py` to the `PATH`

## Uses

`setup_ml.py [Project_PATH] [Option]`

    [Project_PATH]  -  if no path given, current working directory will be taken.

    [Option]
        --normal_lib        - normal ML lib will be added
        --extra_lib         - extra  ML lib will be added
        --no_lib            - NO python lib will be added

to install Libraries:

**Normal Library**

*Numerical Libraries*
- numpy- version = '1.26.4'
- pandas- version = ''
- openpyxl- version = ''

*Machine Learning Libraries*
- scikit-learn- version = ''
- tensorflow- version = ''

*Plotting Libraries*
- seaborn- version = ''
- matplotlib- version = ''
- ipykernel- version = ''
- ipywidgets- version = ''

**Extra**

*Numerical Libraries*
- scipy- version = ''

*Machine Learning Libraries*
- xgboost- version = ''

*Plotting Libraries*
- plotly- version = ''


## Directory Structure
    [Project Directory]
        ├── Data
        |   └── [---]
        ├── Docs
        |   └── [---]
        ├── Model
        |   └── [---]
        ├── Notebook
        |   └── [---]
        ├── pyproject.toml
        ├── README.md
        ├── requirements-dev.lock
        ├── requirements.lock
        └── src
            └── [---]
                └── __init__.py
        
        