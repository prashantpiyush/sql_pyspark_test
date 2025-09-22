from pyspark.sql import *

from pyspark.sql.functions import *

from pyspark.sql.types import *

from prophecy.libs import typed_lit

from pipe1_jobs.pipe1__Reformat_with_random_id.config.ConfigStore import *

from pipe1_jobs.pipe1__Reformat_with_random_id.udfs.UDFs import *


def Reformat_with_random_id(spark: SparkSession, in0: DataFrame) -> DataFrame:
    
            return in0.select(col("id"), col("name").alias("full_name"), col("department"), col("salary"), col("join_date").alias("doj"), lit(43.2).alias("random_id"))
