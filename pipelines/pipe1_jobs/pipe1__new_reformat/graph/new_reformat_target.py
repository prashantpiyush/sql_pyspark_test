from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def new_reformat_target(spark: SparkSession, input_port_1: DataFrame) -> DataFrame:
    # Write to table: `tanmay`.`piyush_test`.`new_reformat`
    input_port_1.write.mode("overwrite").saveAsTable("`tanmay`.`piyush_test`.`new_reformat`")
    return input_port_1
