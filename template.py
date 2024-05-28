import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s : %(message)s]')

package_name= "mongodb_connect"

list_of_file= [
    ".github/workflow/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/maogo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/int.py",
    "init_setup.sh",
    "requirement.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"
]


for path in list_of_file: 
    file_dir, file_name=os.path.split(path)
    # logging.info(f"file directory: {file_dir} for file: {file_name} ")


    if file_dir != "": 
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"logging directory: {file_dir} for file name: {file_name}")

    if (not os.path.exists(path) or (os.path.getsize(path)==0)): 
        with open(path, 'w') as f: 
            pass
            logging.info(f"Creating empty file {path}")
    else: 
        logging.info(f"File is already exits")

        
