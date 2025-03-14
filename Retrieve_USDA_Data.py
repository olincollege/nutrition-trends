from usda.client import UsdaClient
from SecureINformation import API_Key

client =  UsdaClient("OBKSK3PIBmtPIoIxZOUyuttIZIVk9v5vPiMsQBHb")

foods = client.list_foods(5)

for food in foods:
    print(food.name)

#usdaclinet = UsdaClient(API_Key)

#for value in usdaclinet.list_nutrients(10, sort="r"):
#    print(value)
#


##THIS DOES NOT WORK BTW