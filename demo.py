import os
from insurance.exception import InsuranceException
from insurance.pipeline.pipeline import Pipeline
from insurance.logger import logging
from insurance.config.configuration import Configuration
from insurance.component.data_transformation import DataTransformation


def main():
    try:
        config_path = os.path.join("config", "config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        #pipeline = Pipeline()
        # pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        #data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)
        #schema_file_path = r"E:\python\project\project_ml\config\schema.yaml"
        #file_path = r"E:\python\project\project_ml\insurance\artifact\data_ingestion\2022-07-28_21-29-39\ingested_data\train\insurance.csv"
        # df = DataTransformation.load_data(
        #   file_path=file_path, schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
