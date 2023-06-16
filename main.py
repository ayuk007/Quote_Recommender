from src.Quote_Recommender import logger
from src.Quote_Recommender.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_in = DataIngestionPipeline()
        data_in.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    
    except Exception as e:
        logger.exception(e)
        raise e