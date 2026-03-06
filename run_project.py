from src.data_loader import create_spark_session, load_data
from src.data_cleaning import clean_data
from src.trend_analysis import sales_trend_by_date, top_products, regional_sales
from src.visualization import plot_sales_trend


def main():

    # create spark session
    spark = create_spark_session()

    # load dataset
    data = load_data(spark)

    print("Dataset Loaded")
    data.show(5)

    # clean data
    cleaned_data = clean_data(data)

    print("Data Cleaned")

    # trend analysis
    sales_trend = sales_trend_by_date(cleaned_data)
    top_prod = top_products(cleaned_data)
    regional = regional_sales(cleaned_data)

    print("Sales Trend")
    sales_trend.show()

    print("Top Products")
    top_prod.show(10)

    print("Regional Sales")
    regional.show()

    # visualization
    plot_sales_trend(sales_trend)

    print("Visualization saved in Result folder")


if __name__ == "__main__":
    main()