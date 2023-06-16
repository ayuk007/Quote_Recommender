import os
from box.exceptions import BoxValueError
import yaml
from src.Quote_Recommender import logger
import pickle
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args: 
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose = False):
    """create list of direcctories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories is to be created. Defaults to Flase.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_pickle(data: Any, path: Path):
    """save pickle data

    Args:
        data (Any): data to be saved in pickle file
        path (Path): path to pickle file
    """
    pickle.dump(data, open(path, 'wb'))
    
    logger.info(f"pickle file saved at: {path}")

@ensure_annotations
def load_pickle(path: Path):
    """save pickle data

    Args:
        path (Path): path to pickle file
    
    Return:
        data that pickle file contains
    """
    data = pickle.load(open(path, 'rb'))
    
    logger.info(f"pickle file loaded from: {path}")

    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path of the file
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"