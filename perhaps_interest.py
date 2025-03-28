"""This goes through mulitple CSV files to figure out
what foods a collection of households bought over the
course of a year to see total consumption of specific nutrients
"""

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")  # use this if you are not dual booted/WSL

# Load FoodAPS CSV
fah_items = pd.read_csv("csv_data/faps_fahitem_puf.csv", encoding="latin-1")
fah_nutrients = pd.read_csv(
    "csv_data/faps_fahnutrients.csv", encoding="latin-1"
)
fahevent = pd.read_csv("csv_data/faps_fahevent_puf.csv", encoding="latin-1")


def merge_items_with_nutrient(fah_items, fah_nutrients, fahevent):
    """
    Merge food-at-home item purchases with event dates and nutrient info.

    Parameters:
        fah_items (DataFrame): Food-at-home item purchases
        fah_nutrients (DataFrame): Nutrient information
        fahevent (DataFrame): Event-level info with purchase date

    Returns:
        DataFrame: Merged dataset with date and nutrient values
    """
    # Merge item purchases with events to get date
    merged = fah_items.merge(
        fahevent[["eventid", "date"]], on="eventid", how="left"
    )

    # Merge with nutrient values
    merged = merged.merge(fah_nutrients, on=["eventid", "itemnum"], how="left")

    # Convert date column to datetime format
    merged["date"] = pd.to_datetime(merged["date"], errors="coerce")

    # Drop rows without a valid date
    merged = merged.dropna(subset=["date"])

    return merged


def main():
    """need to add a docstring"""
    merged_data = merge_items_with_nutrient(fah_items, fah_nutrients, fahevent)

    # Create 'month' column and group by month
    merged_data["month"] = merged_data["date"].dt.to_period("M")
    monthly_nutrients = (
        merged_data.groupby("month")[
            ["protein", "add_sugars", "carb", "totfat"]
        ]
        .sum()
        .reset_index()
    )
    monthly_nutrients["month"] = monthly_nutrients["month"].dt.to_timestamp()

    # Plot nutrient trends
    plt.figure(figsize=(12, 6))
    for nutrient in ["protein", "add_sugars", "carb", "totfat"]:
        plt.plot(
            monthly_nutrients["month"],
            monthly_nutrients[nutrient],
            label=nutrient,
        )

    plt.title("Monthly Nutrient Consumption from Food-at-Home Purchases")
    plt.xlabel("Month")
    plt.ylabel("Total Nutrient Amount")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(
        "monthly_nutrients_plot.png"
    )  # Saves the plot as a file (works even if matplotlib.use("Agg"))
    print("Plot saved as 'monthly_nutrients_plot.png'")


if __name__ == "__main__":
    main()
