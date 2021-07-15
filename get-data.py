# Import all required packages
import requests, random

# Make request and parse
r = requests.get('http://status.vatsim.net/status.json').json()

# VATSIM Data Link variable
vatsimDataLink = r["data"]["v3"]

# Get random link to download
linkToDownload = random.choice(vatsimDataLink)

# Download the file
with open('vatsim-data.json', 'w+') as out:
    # send request
    r = requests.get(linkToDownload)

    # save data
    out.write(r.text)
