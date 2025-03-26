import requests
import json
import os

url = "https://api.nal.usda.gov/fdc/v1/foods/list?api_key="

with open("key.txt", "r") as file:
    key = file.read()

url += key

print(url)

list_of_food = []
params = {"pageSize": 200, "pageNumber": 1}


r = requests.get(url, params=params)
foodlist = json.loads(r.text)
print(type(foodlist))
print(foodlist[10])
list_of_food.extend(foodlist)
with open("test2.json", "w") as json_file:
    json.dump(foodlist, json_file, indent=4)


i = 2

while True:
    last_description = foodlist[-1].get("description", "")
    if last_description.lower().startswith("z"):
        break

    params = {"pageSize": 200, "pageNumber": i}
    r = requests.get(url, params=params)
    foodlist = json.loads(r.text)

    list_of_food.extend(foodlist)

    for j in range(len(foodlist)):
        print(foodlist[j]["description"])

    print("Length: ", len(foodlist))

    with open("temp.json", "w") as json_file:
        json.dump(foodlist, json_file, indent=4)
        json_file.seek(0)
        json_file.write(" ")
    
    with open("temp.json", "r") as json_file:
        source = json_file.read()
    
    with open("test2.json", "rb+") as json_file:
        json_file.seek(-1, os.SEEK_END)
        comma = ","
        json_file.write(comma.encode('utf-8'))

    with open("test2.json", "a") as json_file:
        json_file.write(source)

    i += 1


# import requests
# import json

# url = "https://api.nal.usda.gov/fdc/v1/foods/list?api_key="

# with open('key.txt', 'r') as file:
#     key = file.read()

# url += key

# print(url)

# list_of_food = []
# params = {"pageSize": 10}

# r = requests.get(url, params=params)
# foodlist = json.loads(r.text)
# print(foodlist)
# i = 0

# while "z" or "Z" in description[0]:

#     params = {"pageSize": 200, "pageNumber": i}

#     r = requests.get(url, params=params)
#     foodlist = json.loads(r.text)

#     list_of_food.append(foodlist)

#     for j in range(len(foodlist)):
#         print(foodlist[j]["description"])

# print("Length: ", len(foodlist))
