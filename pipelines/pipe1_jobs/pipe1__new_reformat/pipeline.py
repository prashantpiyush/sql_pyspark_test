from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipe1__new_reformat.config.ConfigStore import *
from pipe1__new_reformat.udfs.UDFs import *
from prophecy.utils import *
from pipe1__new_reformat.graph import *

def pipeline(spark: SparkSession) -> None:
    df_employee_records = employee_records(spark)
    df_Reformat_1 = Reformat_1(spark, df_employee_records)
    df_new_reformat = new_reformat(spark, df_Reformat_1)
    df_new_reformat_target = new_reformat_target(spark, df_new_reformat)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline - pipe1__new_reformat")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipe1__new_reformat")
    registerUDFs(spark)
    
    pipeline(spark)

if __name__ == "__main__":
    main()
