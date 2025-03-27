import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Load FoodAPS CSV
df = pd.read_csv("csv_data/faps_fahnutrients.csv", encoding="latin-1")

# Daily FDA values for 2000 calorie diet (grams)
daily_values_dict = {"protein": 50, "totfat": 78, "carb": 275, "totsug": 50}

# Group total nutrients per household
household_totals = df.groupby("hhnum")[list(daily_values_dict.keys())].sum()

# Calculate average intake across all households
avg_consumed = household_totals.mean()

# Extract DVs and align them to column names
nutrient_labels = {
    "protein": "Protein",
    "totfat": "Fat",
    "carb": "Carbohydrates",
    "totsug": "Sugars",
}

# Prepare bar chart data
nutrients = list(daily_values_dict.keys())
consumed_vals = [avg_consumed[n] for n in nutrients]
dv_vals = [daily_values_dict[n] for n in nutrients]
labels = [nutrient_labels[n] for n in nutrients]

# Convert to stacked bar components:
under_dv = []
over_dv = []

for consumed, dv in zip(consumed_vals, dv_vals):
    if consumed <= dv:
        under_dv.append(consumed)
        over_dv.append(0)
    else:
        under_dv.append(dv)
        over_dv.append(consumed - dv)

# Plot

fig, ax = plt.subplots(figsize=(10, 6))

bar1 = ax.bar(labels, under_dv, label="Consumed (within DV)", color="skyblue")
bar2 = ax.bar(
    labels, over_dv, bottom=under_dv, label="Consumed (over DV)", color="salmon"
)
bar3 = ax.bar(labels, dv_vals, alpha=0.3, label="FDA Daily Value", color="gray")

ax.set_ylabel("Grams")
ax.set_title("Average Nutrient Consumption vs FDA Daily Values")
ax.legend()
ax.grid(axis="y")
plt.tight_layout()

plt.savefig("dv_stacked_chart.png")

print("Saved stacked bar chart as dv_stacked_chart.png")

# import pandas as pd

# import matplotlib

# matplotlib.use("Agg")
# import matplotlib.pyplot as plt

# df = pd.read_csv("csv_data/faps_fahnutrients.csv")

# print(df.columns)  # checking what columns we can use

# dv_percent = pd.DataFrame()

# # daily values found from FDA for a 2000 calorie budget, all in grams
# daily_values_dict = {"protein": 50, "totfat": 78, "carb": 275, "totsug": 50}

# household_totals = df.groupby("hhnum")[list(daily_values_dict.keys())].sum()


# def calculate_percent_dv(household_totals, daily_values):
#     """docstring yap needs to go here, but this thingies sees what the percent of the daily value that each househodl ate"""
#     result = pd.DataFrame()
#     result["household_num"] = (
#         household_totals.index
#     )  # Set household number column

#     for nutrient, recommended_dv in daily_values.items():
#         actual_amount = household_totals[nutrient]
#         percent_dv = (actual_amount / recommended_dv) * 100

#         # Store in the results table
#         result[nutrient] = actual_amount
#         result[nutrient + "_percent_DV"] = percent_dv

#     return result


# dv_percent_df = calculate_percent_dv(household_totals, daily_values_dict)

# print(dv_percent_df.head())

# plt.figure(figsize=(8, 6))
# dv_percent_df.plot(kind="bar", color="skyblue")
# plt.title("Average % of FDA Daily Value (DV) Achieved from Food Purchases")
# plt.ylabel("Percent of DV (%)")
# plt.xticks(rotation=45)
# plt.grid(axis="y")
# plt.tight_layout()
# plt.savefig("dv_percent_chart.png")
# print("Saved chart as dv_percent_chart.png")
