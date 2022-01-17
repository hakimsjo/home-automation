import requests
import clipboard
import json
import webbrowser
import shortcuts

url = "https://api.easee.cloud/api/accounts/login"
chargerID = "yourid"
payload = "{\"userName\":\"your@email.com\",\"password\":\"yourpassword\"}"

headers = {
	"Accept": "application/json",
	"Content-Type": "application/*+json"
}

response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)

d = json.loads(response.text)
bearer = d.get("accessToken")
#print(bearer)

chargerID = "yourid"
url = "https://api.easee.cloud/api/chargers/" + chargerID + "/state"

headers = {
	"Accept": "application/json",
	"Authorization": "Bearer " + bearer
}

response = requests.request("GET", url, headers=headers)

#print(response.text)

clipboard.set(response.text)

webbrowser.open('shortcuts://callback?callback=x-success')

quit()

