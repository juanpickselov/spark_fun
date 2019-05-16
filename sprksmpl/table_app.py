from pyspark.sql import SparkSession

from table_maker import make_the_table


def table_app():
    spark_sess = SparkSession.builder.appName('ItemListing').enableHiveSupport().getOrCreate()
    make_the_table(spark_sess)

if __name__ == "__main__":
    table_app()
