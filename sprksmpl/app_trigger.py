from pyspark.sql import SparkSession

from read_my_data import read_the_data
from write_my_data import write_the_data
from table_maker import make_the_table


def trigger_app():
    spark_sess = SparkSession.builder.appName('SparkySpark').enableHiveSupport().getOrCreate()
    txt_file_df = read_the_data(spark_sess)
    write_the_data(spark_sess, txt_file_df)
    make_the_table(spark_sess)

if __name__ == "__main__":
    trigger_app()
