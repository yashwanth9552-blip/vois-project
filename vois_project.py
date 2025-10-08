import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

file_path = Path(r"C:\Users\Yashwanth R\Downloads\1730285881-Airbnb_Open_Data.xlsx") #change this file name
df = pd.read_excel(file_path, sheet_name="in")
print("✅ Dataset Loaded Successfully")
print("Shape of dataset:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
df.drop_duplicates(inplace=True)
df = df.dropna(subset=["price", "neighbourhood group", "availability 365"])
df = df[df["price"] < 1000]
avg_price_neigh = df.groupby("neighbourhood group")["price"].mean().sort_values(ascending=False)
print("\n📊 Average Price per Neighbourhood Group:")
print(avg_price_neigh)
top_reviewed = (
    df[["NAME", "number of reviews"]]
    .dropna()
    .sort_values(by="number of reviews", ascending=False)
    .head(10)
)
print("\n⭐ Top 10 Most Reviewed Listings:")
print(top_reviewed)
avg_availability = df.groupby("neighbourhood group")["availability 365"].mean().sort_values(ascending=False)
print("\n📅 Average Availability (days/year) per Neighbourhood Group:")
print(avg_availability)
plt.figure(figsize=(8,5))
df["price"].hist(bins=50, edgecolor="black")
plt.title("Price Distribution of Airbnb Listings")
plt.xlabel("Price ($)")
plt.ylabel("Number of Listings")
plt.xlim(0, 500)   
plt.show()
plt.figure(figsize=(8,5))
sns.barplot(x=avg_price_neigh.index, y=avg_price_neigh.values, palette="viridis")
plt.title("Average Price per Neighbourhood Group")
plt.ylabel("Average Price ($)")
plt.xlabel("Neighbourhood Group")
plt.show()
plt.figure(figsize=(8,5))
sns.barplot(x=avg_availability.index, y=avg_availability.values, palette="magma")
plt.title("Average Availability (Days per Year) by Neighbourhood Group")
plt.ylabel("Average Availability (days)")
plt.xlabel("Neighbourhood Group")
plt.show()
avg_price_neigh.to_csv("avg_price_by_neighbourhood.csv")
top_reviewed.to_csv("top_reviewed_listings.csv", index=False)
avg_availability.to_csv("avg_availability_by_neighbourhood.csv")

print("\n✅ Analysis complete. Results saved as CSV files.")
