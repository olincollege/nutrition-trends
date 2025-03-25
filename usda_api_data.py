import requests
import json

url = "https://api.nal.usda.gov/fdc/v1/foods/list?api_key="

with open("key.txt", "r") as file:
    key = file.read()

url += key

print(url)

list_of_food = []
params = {"pageSize": 200, "pageNumber": 1}

r = requests.get(url, params=params)
foodlist = json.loads(r.text)
print(foodlist)
i = 0

with open("test.json", "w") as json_file:
    json.dump(foodlist, json_file, indent=4)

# while True:
#     last_description = foodlist[-1].get("description", "")
#     if last_description.lower().startswith('z'):
#         break

#     params = {"pageSize": 200, "pageNumber": i}
#     r = requests.get(url, params=params)
#     foodlist = json.loads(r.text)

#     list_of_food.append(foodlist)

#     for j in range(len(foodlist)):
#         print(foodlist[j]["description"])

#     print("Length: ", len(foodlist))
#     i += 1


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
