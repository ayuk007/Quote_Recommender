from src.Quote_Recommender.constants import *
from src.Quote_Recommender.utils.common import read_yaml, create_directories
from src.Quote_Recommender.entity.config_entity import (DataIngestionConfig)
from pathlib import Path

class ConfigManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH ):
        
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        params = self.params.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            save_path = config.save_path,
            tags = params.tags,
            num_pages = params.num_pages
        )
    
        return data_ingestion_config