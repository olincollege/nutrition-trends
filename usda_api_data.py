"""This code loads data into a JSON file"""

import json
import os
import requests

URL = "https://api.nal.usda.gov/fdc/v1/foods/list?api_key="

# This is the API key file
with open("key.txt", "r", encoding="utf-8") as file:
    key = file.read()

URL += key

print(URL)

list_of_food = []
params = {"pageSize": 200, "pageNumber": 1}


r = requests.get(URL, params=params, timeout=10)
foodlist = json.loads(r.text)
print(type(foodlist))
print(foodlist[10])
list_of_food.extend(foodlist)
with open("food_nutrition.json", "w", encoding="utf-8") as json_file:
    json.dump(foodlist, json_file, indent=4)


i = 2

while True:
    last_description = foodlist[-1].get("description", "")
    if last_description.lower().startswith("z"):
        break

    params = {"pageSize": 200, "pageNumber": i}
    r = requests.get(URL, params=params, timeout=10)
    foodlist = json.loads(r.text)

    list_of_food.extend(foodlist)

    for j in range(len(foodlist)):
        print(foodlist[j]["description"])

    print("Length: ", len(foodlist))

    with open("temp.json", "w", encoding="utf-8") as json_file:
        json.dump(foodlist, json_file, indent=4)
        json_file.seek(0)
        json_file.write(" ")

    with open("temp.json", "r", encoding="utf-8") as json_file:
        source = json_file.read()

    with open("food_nutrition.json", "rb+") as json_file:
        json_file.seek(-1, os.SEEK_END)
        COMMA = ","
        json_file.write(COMMA.encode("utf-8"))

    with open("food_nutrition.json", "a") as json_file:
        json_file.write(source)

    i += 1
