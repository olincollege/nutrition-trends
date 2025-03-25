import json

with open("cry.json", encoding="utf-8") as file:
    data_string = file.read()
    data = json.loads(data_string)

print(data)

# food_list = [
#     data['description'],
#     "Pizza",
#     "Fried Chicken",
#     "Mac and Cheese",
#     "Hot Dogs",
#     "Sandwiches",
#     "Spaghetti with Meatballs",
#     "Tacos",
#     "Salads",
#     "Pancakes",
# ]


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

    ##This part is definitely wrong but I have no idea what I am doing
    nutrient_list = []
    for i in data[food]:
        # protein
        if i.get("number") == "203":
            nutrient_list.append(i.get("amount"))
        # fatty acids
        if i.get("number") == "606":
            nutrient_list.append(i.get("amount"))
        # carbohydrates
        if i.get("number") == "205":
            nutrient_list.append(i.get("amount"))
        # sugars
        if i.get("number") == "269":
            nutrient_list.append(i.get("amount"))
        return nutrient_list


# food_dict = {}
# for i in food_list:
#     food_dict[i] = get_food_details(i)
