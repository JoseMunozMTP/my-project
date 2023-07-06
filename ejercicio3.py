import requests, json

# Request GET a una API
url = "https://mtp.alejmans.dev/maas/proxy/test/suma"
parametros = "a=1&b=2"

response = requests.get(url, params=parametros)
print(response.text)



# Request POST a una API
url = "https://mtp.alejmans.dev/maas/proxy/test/suma"
data = '{"a":1,"b":2}'  # json

response = requests.post(url, data=data)
print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)