import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
#orig = "Rome, Italy"
#dest = "Frascati, Italy"
key = "Qn56rlHCDBVtBisnWdE5MP8T3mO99M1B"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()

print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
