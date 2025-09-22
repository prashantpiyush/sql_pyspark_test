from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipe1_jobs.pipe1__Reformat_with_random_id.config.ConfigStore import *
from pipe1_jobs.pipe1__Reformat_with_random_id.udfs.UDFs import *
from prophecy.utils import *
from pipe1_jobs.pipe1__Reformat_with_random_id.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Reformat_1 = Reformat_1(spark)
    df_Reformat_with_random_id = Reformat_with_random_id(spark, df_Reformat_1)
    df_Reformat_with_random_id_target = Reformat_with_random_id_target(spark, df_Reformat_with_random_id)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline - pipe1__Reformat_with_random_id")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipe1__Reformat_with_random_id")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipe1__Reformat_with_random_id", config = Config)(pipeline)

if __name__ == "__main__":
    main()
