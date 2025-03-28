"""This goes through multiple CSV files to figure out what foods a
collection of households bought over time. By also checking, how
much more it is than the daily value required for a balanced 2000 calorie diet.
"""

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")  # use this if you are not dual booted/WSL

df = pd.read_csv("csv_data/faps_fahnutrients.csv", encoding="latin-1")

# Daily FDA values for 2000 calorie diet (grams)
daily_values_dict = {"protein": 50, "totfat": 78, "carb": 275, "totsug": 50}

nutrient_labels = {
    "protein": "Protein",
    "totfat": "Fat",
    "carb": "Carbohydrates",
    "totsug": "Sugars",
}

nutrients = list(daily_values_dict.keys())


# looping through each household and summing their nutrient intake
def get_household_totals(data, nutrients):
    """
    Goes through each household and adds up all the nutrients they bought.
    Returns a DataFrame where each row is one household
    and the total nutrients they got.
    """
    households = data["hhnum"].unique()  # all of the household ids
    household_totals = []

    for hh in households:
        hh_data = data[data["hhnum"] == hh]
        totals = {"hhnum": hh}
        for nutrient in nutrients:
            totals[nutrient] = hh_data[nutrient].sum()
        household_totals.append(totals)

    return pd.DataFrame(household_totals)


household_totals_df = get_household_totals(df, nutrients)

# print("Available columns:", household_totals_df.columns.tolist())

avg_grams_consumed = household_totals_df[nutrients].mean()

percent_dv_consumed = {
    nutrient: (avg_grams_consumed[nutrient] / dv) * 100
    for nutrient, dv in daily_values_dict.items()
}


def split_dv_levels(percent_dv, nutrient_labels):
    """
    Splits each nutrient into how much was under
    100% of DV and how much was over.
    Returns three lists: labels, under_dv, over_dv.
    """
    # breaking down the households' averages
    under_dv = []
    over_dv = []
    labels = []

    for nutrient, percent in percent_dv.items():
        label = nutrient_labels[nutrient]
        labels.append(label)

        if percent <= 100:
            under_dv.append(percent)
            over_dv.append(0)
        else:
            under_dv.append(100)
            over_dv.append(percent - 100)

    return labels, under_dv, over_dv


labels, under_dv, over_dv = split_dv_levels(
    percent_dv_consumed, nutrient_labels
)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(labels, under_dv, label="Consumed (within DV)", color="blue")
ax.bar(
    labels, over_dv, bottom=under_dv, label="Consumed (over DV)", color="purple"
)

# 100% DV
ax.axhline(100, color="red", linestyle="--", linewidth=1.2, label="100% DV")

ax.set_ylabel("Percent of Daily Value (%)")
ax.set_title("Average Nutrient Intake as % of FDA Daily Value")
ax.legend()
ax.grid(axis="y")
plt.tight_layout()  # helps to avoid overlap
plt.savefig("dv_stacked_chart.png")
