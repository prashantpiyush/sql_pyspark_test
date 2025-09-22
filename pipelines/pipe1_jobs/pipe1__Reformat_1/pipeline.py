from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipe1_jobs.pipe1__Reformat_1.config.ConfigStore import *
from pipe1_jobs.pipe1__Reformat_1.udfs.UDFs import *
from prophecy.utils import *
from pipe1_jobs.pipe1__Reformat_1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_employee_records = employee_records(spark)
    df_Reformat_1 = Reformat_1(spark, df_employee_records)
    df_Reformat_1_target = Reformat_1_target(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline - pipe1__Reformat_1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipe1__Reformat_1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipe1__Reformat_1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
