from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def Reformat_1_target(spark: SparkSession, input_port_0: DataFrame) -> DataFrame:
    # Write to table: `tanmay`.`piyush_test`.`Reformat_1`
    input_port_0.write.mode("overwrite").saveAsTable("`tanmay`.`piyush_test`.`Reformat_1`")
    return input_port_0
