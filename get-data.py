# Import all required packages
import urllib3, random

# VATSIM Data Link variable
vatsimDataLink = []

# client
http = urllib3.PoolManager()

# send request
r = http.request(
            "GET", 
            "http://status.vatsim.net",
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
)

# get data
data = r.data.decode('utf-8').split("\r\n")

# Iterate over data
for line in data:
    # Check if json3 exists
    if "json3=" in line:
        # If exists, split data and get the link
        vatsimDataLink.append(line.split("=")[1])

# Get random link to download
linkToDownload = random.choice(vatsimDataLink)

# Download the file
with open('vatsim-data.json', 'w+') as out:
    # send request
    r = http.request('GET', linkToDownload)

    # read data
    data = r.data.decode('utf-8')

    # save data
    out.write(data)