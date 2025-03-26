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

# putting keys in dict
american_food_matched = {key: None for key in american_food_keys}

for food in data:
    description = food.get("description", "").lower()
    print("Checking USDA description:", description)
    for general_food in american_food_keys:
        if general_food.lower() in description:
            print(f"Matched '{general_food}' with USDA item: {description}")
            if american_food_matched[general_food] is None:
                american_food_matched[general_food] = (
                    food  # Save the whole USDA food item
                )

print(american_food_matched)

# where the ifstatement/function needs to be to make the general food name to the USDA description

# what i need to do
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

#     ##This part is definitely wrong but I have no idea what I am doing
#     nutrient_list = []
#     for i in data[food]:
#         # protein
#         if i.get("number") == "203":
#             nutrient_list.append(i.get("amount"))
#         # fatty acids
#         if i.get("number") == "606":
#             nutrient_list.append(i.get("amount"))
#         # carbohydrates
#         if i.get("number") == "205":
#             nutrient_list.append(i.get("amount"))
#         # sugars
#         if i.get("number") == "269":
#             nutrient_list.append(i.get("amount"))
#         return nutrient_list


# food_dict = {}
# for i in american_food_list:
#     food_dict[i] = get_food_details(i)
