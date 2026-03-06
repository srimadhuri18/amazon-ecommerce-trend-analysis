from pyspark.sql import SparkSession


def create_spark_session():

    spark = SparkSession.builder \
        .appName("Amazon Sales Trend Analysis") \
        .getOrCreate()

    return spark


def load_data(spark):

    data = spark.read.csv(
        "Data/amazon_sales.csv",
        header=True,
        inferSchema=True
    )

    return data