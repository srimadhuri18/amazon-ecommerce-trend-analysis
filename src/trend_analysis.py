from pyspark.sql.functions import sum, col


def sales_trend_by_date(data):

    trend = data.groupBy("Order Date") \
        .agg(sum("Sales").alias("Total_Sales")) \
        .orderBy("Order Date")

    return trend


def top_products(data):

    products = data.groupBy("Product Name") \
        .agg(sum("Sales").alias("Total_Sales")) \
        .orderBy(col("Total_Sales").desc())

    return products


def regional_sales(data):

    region_sales = data.groupBy("Region") \
        .agg(sum("Sales").alias("Total_Sales")) \
        .orderBy(col("Total_Sales").desc())

    return region_sales