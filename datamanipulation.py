import json

with open("test.json", encoding="utf-8") as file:
    data_string = file.read()
    data = json.loads(data_string)

# Preset the keys to know what the food is initailly

# Top american foods according to google
american_food_keys = [
    "Pizza",
    "Fried Chicken",
    "Mac and Cheese",
    "Hot Dogs",
    "Sandwiches",
    "Spaghetti with Meatballs",
    "Tacos",
    "Salads",
    "Pancakes",
]
# preseting the intial food in the dictionary
matched_food = {key: None for key in american_food_keys}
print(matched_food)

for food in data:
    description = food.get(
        "description", ""
    ).lower()  # defines description in USDA data and makes it all lowercase
    print("Checking USDA description:", description)

    for american_food in american_food_keys:  # start of the for loop
        if american_food.lower() in description:
            # print(f"Matched '{american_food}' with USDA item: {description}")
            if matched_food[american_food] is not None:
                pass  # Do nothing if the condition is false
            elif matched_food[american_food] is None:
                matched_food[american_food] = (
                    food  # Save the whole USDA food item
                )
            else:
                pass  # Do nothing if the condition is false

print(matched_food)


# def esther_suffer(food):
#     """this is what I hate"""
#     matched_food = {key: None for key in american_food_keys}


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
    nutrient_list = []

    for nutrient in food.get("foodNutrients", []):
        if nutrient.get("number") == "203":  # protein
            nutrient_list.append(nutrient.get("amount"))
        elif nutrient.get("number") == "606":  # fatty acids
            nutrient_list.append(nutrient.get("amount"))
        elif nutrient.get("number") == "205":  # carbohydrates
            nutrient_list.append(nutrient.get("amount"))
        elif nutrient.get("number") == "269":  # sugars
            nutrient_list.append(nutrient.get("amount"))

    return nutrient_list


# def get_food_details(food):
#     """
#     This function takes the food name/id/description and returns the amounts
#     of 4 certain nutrients (protein, fatty acids, Carbohydrates, and Sugars)
#     in the form of a list ordered the same way it is above

#     Args:
#         food: a string that represents the food being searched
#     Returns:
#         a new list that consists of the food as keys and the 4 nutrient
#         amounts as the values
#     """

#     # This part is definitely wrong but I have no idea what I am doing
#     nutrient_list = []
#     amount = food.get("amount", "")
#     number = food.get("number", "")

#     for american_food, value in matched_food():
#         # protein
#         if i.get(number) == "203":
#             nutrient_list.append(i.get(amount))
#         # fatty acids
#         if i.get(number) == "606":
#             nutrient_list.append(i.get(amount))
#         # carbohydrates
#         if i.get(number) == "205":
#             nutrient_list.append(i.get(amount))
#         # sugars
#         if i.get(number) == "269":
#             nutrient_list.append(i.get(amount))
#         return nutrient_list

# ##This part is definitely wrong but I have no idea what I am doing
# nutrient_list = []
# for i in data[food]:
#     # protein
#     if i.get("number") == "203":
#         nutrient_list.append(i.get("amount"))
#     # fatty acids
#     if i.get("number") == "606":
#         nutrient_list.append(i.get("amount"))
#     # carbohydrates
#     if i.get("number") == "205":
#         nutrient_list.append(i.get("amount"))
#     # sugars
#     if i.get("number") == "269":
#         nutrient_list.append(i.get("amount"))
#     return nutrient_list


food_dict = {}

for food_name, usda_item in matched_food.items():
    if usda_item:  # not None
        food_dict[food_name] = get_food_details(usda_item)
    else:
        food_dict[food_name] = None


print(food_dict)
