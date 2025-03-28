import json
import matplotlib.pyplot as plt

with open("food_nutrition.json", encoding="utf-8") as file:
    data_string = file.read()
    data = json.loads(data_string)

# Preset the keys to know what the food is initailly

# Top american foods according to google
american_food_keys = [
    "Fast Food, Pizza",
    "Fried Chicken",
    "Hamburger",
    "Hot Dog",
    "Grilled Cheese Sandwich",
    "Spaghetti with Meatballs",
    "Taco",
    "Caesar Salad",
    "Pancakes",
]
# preseting the intial food in the dictionary
matched_food = {key: None for key in american_food_keys}
# print(matched_food)

for food in data:
    description = food.get("description", "").lower()

    for american_food in american_food_keys:
        if american_food.lower() in description:
            # print(f"Matched '{american_food}' with USDA item: {description}")
            if matched_food[american_food] is not None:
                pass  # Do nothing if the condition is false
            elif matched_food[american_food] is None:
                matched_food[american_food] = food
            else:
                pass

print(matched_food)


def get_food_details(food):
    """
    This function takes the food name/id/description and returns the amounts
    of 4 certain nutrients (protein, fatty acids, Carbohydrates, and Sugars)
    in the form of a list ordered the same way it is above

    Args:
        food: a string that represents the food being searched
    Returns:
        a new list that consists of the food as keys and the 4 nutrient
        amounts as the values
    """
    nutrient_order = {
        "203": 0,  # Protein
        "606": 1,  # Fatty Acids
        "205": 2,  # Carbohydrates
        "269": 3,  # Sugars
        "291": 4,  # Fiber
        "307": 5,  # Sodium
        "255": 6,  # Water
    }
    nutrient_list = [0] * 7

    for nutrient in food.get("foodNutrients", []):
        nutrient_number = nutrient.get("number")
        if nutrient_number in nutrient_order:
            nutrient_list[nutrient_order[nutrient_number]] = nutrient.get(
                "amount"
            )

    return nutrient_list


food_dict = {}

for food_name, usda_item in matched_food.items():
    if usda_item:  # Ensure the item is not None
        food_dict[food_name] = get_food_details(usda_item)
    else:
        food_dict[food_name] = [0] * 7

print(food_dict)

# this code gives us the total nutrients of the top 10 most eaten foods
total_nutrients = []
list_len = [0, 1, 2, 3, 4, 5, 6]
for i in list_len:
    total_one_nutrient = sum(values[i] for values in food_dict.values())
    total_nutrients.append(total_one_nutrient)
print(total_nutrients)


# order is proteins, fats, carbs, sugars, fibers, sodium, and water

nrf_score_list = []
for food, values in food_dict.items():
    nrf_score = ((values[0] / 50) + (values[4] / 28) + (values[6] / 500)) - (
        (values[1] / 20)
        + (values[3] / 50)
        + (values[5] / 2000)
        + (values[2] / 275)
    )
    nrf_score_list.append(nrf_score)

plt.bar(american_food_keys, nrf_score_list)
plt.title("NRF Score of the 10 most common foods in America")
plt.xlabel("Foods")
plt.ylabel("NRF Score")
plt.show()
