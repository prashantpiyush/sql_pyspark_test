from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def Reformat_with_random_id_target(spark: SparkSession, input_port_2: DataFrame) -> DataFrame:
    # Write to table: `tanmay`.`piyush_test`.`Reformat_with_random_id`
    input_port_2.write.mode("overwrite").saveAsTable("`tanmay`.`piyush_test`.`Reformat_with_random_id`")
    return input_port_2
