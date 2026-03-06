import matplotlib.pyplot as plt


def plot_sales_trend(trend_df):

    trend_pd = trend_df.toPandas()

    plt.figure()

    plt.plot(trend_pd["Order Date"], trend_pd["Total_Sales"])

    plt.xlabel("Order Date")
    plt.ylabel("Total Sales")
    plt.title("Amazon Sales Trend")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("Result/sales_trend.png")

    plt.close()