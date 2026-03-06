from pyspark.sql.functions import col


def clean_data(data):

    # remove null values
    data = data.dropna()

    # remove negative sales
    if "Sales" in data.columns:
        data = data.filter(col("Sales") > 0)

    # remove negative quantity
    if "Quantity" in data.columns:
        data = data.filter(col("Quantity") > 0)

    return data