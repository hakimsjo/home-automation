import requests
import clipboard
import json
import webbrowser

myToken = 'yourtoken'
headers = {'Authorization': "Bearer {}".format(myToken)}
	
# Prices now
params = {"query": 
  "{viewer {homes {currentSubscription{priceInfo{current{total energy tax startsAt}}}}}}"
}

r = requests.get('https://api.tibber.com/v1-beta/gql', headers=headers, params=params)

# Cleanup to flat dictionary
j = r.text.replace('{"data":{"viewer":{"homes":[{"currentSubscription":{"priceInfo":{"current":{', ' ')
j = j.replace('}}}}]}}}',' ')
j = j.replace('"','')

clipboard.set(j)

webbrowser.open('shortcuts://callback?callback=x-success')

quit()


