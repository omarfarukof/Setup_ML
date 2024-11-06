#!/usr/bin/env python3

# Importing Modules
import os
import sys

# Check if rye is available
# print(os.system("rye --version" ))
# exit()
if os.system("rye --version") != 0:
    print("Rye is not available. Exiting. Please install rye and try again.")
    exit(1)

# Take argparse from sys
args = sys.argv[1:]
path = [p for p in args if "--" not in p]
options = [o for o in args if "--" in o]

# Take Project Path
if len(path) == 0:
    local_path = '.'
else:
    local_path = path[0]

# GPU Support
is_gpu = False
if '--gpu' in args:
    print("GPU Libraries will be used ===>")
    is_gpu = True

## ML Dependencies
# Numerical Libraries
_numpy_version = '1.26.4'
_pandas_version = ''
_openpyxl_version = ''

# Machine Learning Libraries
_scikit_learn_version = ''
_tensorflow_version = ''

# Plotting Libraries
_seaborn_version = ''
_matplotlib_version = ''
_ipykernel_version = ''
_ipywidgets_version = ''

## Extra
# Numerical Libraries
_scipy_version = ''

# Machine Learning Libraries
_xgboost_version = ''

# Plotting Libraries
_plotly_version = ''


## Directories
directories = [
    'Notebook',
    'Data',
    'Docs',
    'Model'
]


def pl_ver(pylib:str , version:str = '') -> str:
    if version == '':
        return pylib
    else:
        return pylib + "==" + version


# list of Dependencies
normal_libs = [
    # Numerical Libraries
    pl_ver('numpy', _numpy_version),
    pl_ver('pandas', _pandas_version),
    pl_ver('openpyxl', _openpyxl_version),
    
    # Machine Learning Libraries
    pl_ver('scikit-learn' , _scikit_learn_version),
    pl_ver('tensorflow[and-cuda]' , _tensorflow_version) if is_gpu else pl_ver('tensorflow' , _tensorflow_version),
    
    # Plotting Libraries
    pl_ver('seaborn' , _seaborn_version),
    pl_ver('matplotlib' , _matplotlib_version),
    pl_ver('ipykernel' , _ipykernel_version),
    pl_ver('ipywidgets' , _ipywidgets_version),
]

# list of Extra Dependencies
extra_libs = [
    # Numerical Libraries
    pl_ver('scipy' , _scipy_version),

    # Machine Learning Libraries
    pl_ver('xgboost' , _xgboost_version),

    # Plotting Libraries
    pl_ver('plotly' , _plotly_version),

]



## Setup Functions
def setup_rye(path:str , normal_libs: list, extra_libs: list) -> None:
    # Initialize rye
    print("\nInitializing Rye ====>")
    print("rye init " + path)
    os.system("rye init " + path)
    
    # Change Directory to Project Directory
    print("\ncd " + path)
    os.chdir(path)

    # Install Normal Libraries
    if len(normal_libs) != 0:
        # print("CWD = " + os.getcwd() )
        print("\nInstalling Normal Libraries ====>")
        print("rye add " + " ".join(normal_libs))
        os.system("rye add " + " ".join(normal_libs))
    
    # Install Extra Libraries (if any)
    if len(extra_libs) != 0:
        print("\nInstalling Extra Libraries ====>")
        print("rye add " + " ".join(extra_libs))
        os.system("rye add " + " ".join(extra_libs))
    
    # Syncronize Rye Libraries
    print("\nSyncronizing Rye Libraries ====>")
    print("rye sync")
    os.system("rye sync")


## Setup ML Folders
def setup_ml(path:str , is_normal_lib:bool=True , is_extra_lib:bool=False , norm_lib:list=[], ex_lib:list=[] ) -> None:
    # Create ML Folder
    if is_normal_lib:
        norm_lib = normal_libs
    if is_extra_lib:
        ex_lib = extra_libs

    setup_rye( path , norm_lib , ex_lib)
    
    # Change Directory to Project Directory
    # os.system("cd " + path)


    # Create Folders
    print("\nCreating Folders ====>")
    for d in directories:
        if os.path.exists(d):
            print("Folder '" + d + "' already exists")
        else:
            print("Creating Folder '" + d + "'")
            os.mkdir(d )
    
    # # Print Current Working Directory
    # print("\n" + os.getcwd() )


##========Script Starts Here========##

is_normal_lib = True
is_extra_lib = False

if '--normal_lib' in options:
    print("Normal Libraries will be installed ===>")
    is_normal_lib = True

if '--extra_lib' in options:
    print("Extra Libraries will be installed ===>")
    is_extra_lib = True

if '--no_lib' in options:
    print("No Libraries will be installed ===>")
    is_normal_lib = False
    is_extra_lib = False


setup_ml(local_path , is_normal_lib , is_extra_lib )
# print(local_path)

##========Script Ends Here========##