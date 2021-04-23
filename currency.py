import requests
import json 

m = requests.get('https://api.ratesapi.io/api/latest?base=USD')
data = json.loads(m.text)
rates = data.get('rates')
symbols = rates.keys()
print(symbols)
cur1 = input("Введите валюту:")
cur2 = input("Введите валюту:")
amount = int(input("Введите сумму:"))
print(amount/rates.get(cur1)*rates.get(cur2))
