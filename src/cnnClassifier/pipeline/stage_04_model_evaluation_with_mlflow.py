from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager3



STAGE_NAME = "Evaluation Stage"



class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager3()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
