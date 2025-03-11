from usda.client import UsdaClient
from SecureINformation import API_Key
usdaclinet = UsdaClient(API_Key)

for value in usdaclinet.list_nutrients(10, sort="r"):
    print(value)
