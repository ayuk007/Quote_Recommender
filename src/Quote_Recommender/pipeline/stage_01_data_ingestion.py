from src.Quote_Recommender.config.configuration import ConfigManager
from src.Quote_Recommender.components.data_ingestion import DataIngestion
from src.Quote_Recommender import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_data()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_in = DataIngestionPipeline()
        data_in.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    
    except Exception as e:
        logger.exception(e)
        raise e