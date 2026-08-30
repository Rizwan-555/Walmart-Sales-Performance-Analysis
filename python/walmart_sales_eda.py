import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Walmart_Sales_Cleaned.csv")
df["Date"] = pd.to_datetime(df["Date"])
print("\nData Types After Date Conversion:")
print(df.dtypes)

# Display basic information
print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# Weekly Sales Distribution

plt.figure(figsize=(10, 6))

plt.hist(df["Weekly_Sales"], bins=30, edgecolor="black")

plt.title("Distribution of Weekly Sales")
plt.xlabel("Weekly Sales")
plt.ylabel("Number of Records")

plt.savefig("weekly_sales_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

# Total Sales by Store

store_sales = df.groupby("Store")["Weekly_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))

store_sales.plot(kind="bar")

plt.title("Total Sales by Store")
plt.xlabel("Store")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)

plt.savefig("total_sales_by_store.png", dpi=300, bbox_inches="tight")
plt.close()

# Monthly Sales Trend

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Weekly_Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))

monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.savefig("monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.close()

# Highest and Lowest Sales Months

highest_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

lowest_month = monthly_sales.idxmin()
lowest_sales = monthly_sales.min()

print("\nHighest Sales Month:")
print(highest_month, round(highest_sales, 2))

print("\nLowest Sales Month:")
print(lowest_month, round(lowest_sales, 2))

# Yearly Sales Trend

yearly_sales = (
    df.groupby(df["Date"].dt.year)["Weekly_Sales"]
    .sum()
)

plt.figure(figsize=(10, 6))

yearly_sales.plot(kind="bar")

plt.title("Total Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")

plt.savefig("yearly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.close()

print("\nYearly Sales:")
print(yearly_sales)

# Total Sales by Store

store_sales = (
    df.groupby("Store")["Weekly_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))

store_sales.plot(kind="bar")

plt.title("Total Sales by Store")
plt.xlabel("Store")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)

plt.savefig("total_sales_by_store.png", dpi=300, bbox_inches="tight")
plt.close()

print("\nTop 10 Stores by Total Sales:")
print(store_sales.head(10))

# Holiday vs Non-Holiday Sales

holiday_sales = (
    df.groupby("Holiday_Flag")["Weekly_Sales"]
    .mean()
)

holiday_sales.index = ["Non-Holiday", "Holiday"]

plt.figure(figsize=(8, 6))

holiday_sales.plot(kind="bar")

plt.title("Average Weekly Sales: Holiday vs Non-Holiday")
plt.xlabel("Week Type")
plt.ylabel("Average Weekly Sales")
plt.xticks(rotation=0)

plt.savefig("holiday_vs_nonholiday.png", dpi=300, bbox_inches="tight")
plt.close()

print("\nAverage Weekly Sales - Holiday vs Non-Holiday:")
print(holiday_sales)

# Correlation Analysis

numeric_columns = [
    "Weekly_Sales",
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment"
]

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation.round(3))

# Correlation Heatmap

plt.figure(figsize=(10, 7))

plt.imshow(correlation, interpolation="nearest")
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# Temperature vs Weekly Sales

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Temperature"],
    df["Weekly_Sales"],
    alpha=0.4
)

plt.title("Temperature vs Weekly Sales")
plt.xlabel("Temperature (°)")
plt.ylabel("Weekly Sales")

plt.savefig("temperature_vs_sales.png", dpi=300, bbox_inches="tight")
plt.close()

# Fuel Price vs Weekly Sales

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Fuel_Price"],
    df["Weekly_Sales"],
    alpha=0.4
)

plt.title("Fuel Price vs Weekly Sales")
plt.xlabel("Fuel Price")
plt.ylabel("Weekly Sales")

plt.savefig("fuel_price_vs_sales.png", dpi=300, bbox_inches="tight")
plt.close()

# CPI vs Weekly Sales

plt.figure(figsize=(10, 6))

plt.scatter(
    df["CPI"],
    df["Weekly_Sales"],
    alpha=0.4
)

plt.title("CPI vs Weekly Sales")
plt.xlabel("CPI")
plt.ylabel("Weekly Sales")

plt.savefig("cpi_vs_sales.png", dpi=300, bbox_inches="tight")
plt.close()

# Unemployment vs Weekly Sales

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Unemployment"],
    df["Weekly_Sales"],
    alpha=0.4
)

plt.title("Unemployment vs Weekly Sales")
plt.xlabel("Unemployment (%)")
plt.ylabel("Weekly Sales")

plt.savefig("unemployment_vs_sales.png", dpi=300, bbox_inches="tight")
plt.close()

# Average Weekly Sales by Store

average_store_sales = (
    df.groupby("Store")["Weekly_Sales"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop 10 Stores by Average Weekly Sales:")
print(average_store_sales.head(10))

# Average Sales by Month

monthly_average = (
    df.groupby(df["Date"].dt.month)["Weekly_Sales"]
    .mean()
)

print("\nAverage Weekly Sales by Month:")
print(monthly_average.round(2))

plt.figure(figsize=(10, 6))

monthly_average.plot(kind="bar")

plt.title("Average Weekly Sales by Month")
plt.xlabel("Month")
plt.ylabel("Average Weekly Sales")
plt.xticks(rotation=0)

plt.savefig("average_sales_by_month.png", dpi=300, bbox_inches="tight")
plt.close()

# Bottom 10 Stores by Average Weekly Sales

print("\nBottom 10 Stores by Average Weekly Sales:")
print(average_store_sales.tail(10).sort_values())

# Holiday Sales by Store

holiday_store_sales = (
    df.groupby(["Store", "Holiday_Flag"])["Weekly_Sales"]
    .mean()
    .unstack()
)

holiday_store_sales.columns = ["Non-Holiday", "Holiday"]

print("\nAverage Weekly Sales by Store - Holiday vs Non-Holiday:")
print(holiday_store_sales.head(10))

# Holiday Sales Uplift by Store

holiday_uplift = (
    (holiday_store_sales["Holiday"] - holiday_store_sales["Non-Holiday"])
    / holiday_store_sales["Non-Holiday"]
    * 100
)

holiday_uplift = holiday_uplift.sort_values(ascending=False)

print("\nTop 10 Stores by Holiday Sales Uplift (%):")
print(holiday_uplift.head(10).round(2))

print("\nBottom 10 Stores by Holiday Sales Uplift (%):")
print(holiday_uplift.tail(10).round(2))

# Sales Volatility by Store

store_volatility = (
    df.groupby("Store")["Weekly_Sales"]
    .std()
    .sort_values(ascending=False)
)

print("\nTop 10 Stores by Sales Volatility:")
print(store_volatility.head(10))

print("\nBottom 10 Stores by Sales Volatility:")
print(store_volatility.tail(10))


# Weekly Sales Outlier Detection using IQR

Q1 = df["Weekly_Sales"].quantile(0.25)
Q3 = df["Weekly_Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Weekly_Sales"] < lower_bound) |
    (df["Weekly_Sales"] > upper_bound)
]

print("\nOutlier Detection:")
print("Q1:", round(Q1, 2))
print("Q3:", round(Q3, 2))
print("IQR:", round(IQR, 2))
print("Lower Bound:", round(lower_bound, 2))
print("Upper Bound:", round(upper_bound, 2))
print("Number of Outliers:", len(outliers))
