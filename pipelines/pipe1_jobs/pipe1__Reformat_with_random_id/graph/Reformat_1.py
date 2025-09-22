from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def Reformat_1(spark: SparkSession) -> DataFrame:
    # Read from temp table: `tanmay`.`piyush_test`.`pipe1__Reformat_1`
    return spark.table("`tanmay`.`piyush_test`.`pipe1__Reformat_1`")
