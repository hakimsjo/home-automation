import requests
import clipboard
import json
import webbrowser
import shortcuts

url = "https://api.easee.cloud/api/accounts/login"

payload = "{\"userName\":\"your@email.com\",\"password\":\"yourpassword\"}"
headers = {
	"Accept": "application/json",
	"Content-Type": "application/*+json"
}

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)


url = "https://api.easee.cloud/api/chargers/EHyournumber/state"

headers = {
	"Accept": "application/json",
	"Authorization": "Bearer yourcode"
}

response = requests.request("GET", url, headers=headers)

#print(response.text)

clipboard.set(response.text)

webbrowser.open('shortcuts://callback?callback=x-success')

quit()

