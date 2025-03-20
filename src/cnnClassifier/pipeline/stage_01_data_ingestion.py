from cnnClassifier.config.configuration import ConfigurationManager1
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init_(self):
        pass

    def main(self):
            config = ConfigurationManager1()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f" >>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f" >>>>>> Stage {STAGE_NAME} completed <<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e 
        
        
        