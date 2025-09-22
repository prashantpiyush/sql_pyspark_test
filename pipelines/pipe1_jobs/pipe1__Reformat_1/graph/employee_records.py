from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def employee_records(spark: SparkSession) -> DataFrame:
    # Read from catalog table: `tanmay`.`piyush_test`.`employees`
    return spark.table("`tanmay`.`piyush_test`.`employees`")
