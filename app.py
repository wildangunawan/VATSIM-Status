# API for VATSIM data
# made by Wildan Gunawan 1300014
# Contact: me@wildan.web.id

# import required libraries
import json

# get the data
with open("vatsim-data.json", "r", errors="ignore") as f:
    # import JSON as python dictionary
    data = json.load(f)

# Set all variable to store
# client and server data
dataserver = {}
dataclient_ATC = {}
dataclient_PILOT = {}

# data yang gak diambil
data_delete_ATC = ["altitude", "groundspeed", "heading", "qnh_i_hg", "qnh_mb", "transponder", "planned"]
data_delete_pilot = ["atis_message", "facilitytype", "visualrange", "rating"]

# for loop over data
for key, value in data.items():
    # check which key right now
    if key == "clients":
        # loop over client data
        for client in value:
            data_baru = {}
            
            # if client is ATC
            if client['clienttype'] == "ATC":
                
                # for loop over client data
                for key, value in client.items():
                    # cek kalo key nggak diambil
                    if "planned" not in key and key not in data_delete_ATC:
                        data_baru[key] = value
                
                # save in client data variable
                dataclient_ATC[client['callsign']] = data_baru
                
            # if client is pilot
            elif client['clienttype'] == "PILOT":
                
                # cek kalo key nggak diambil
                for key, value in client.items():
                    
                    # cek kalo key nggak diambil
                    if key not in data_delete_pilot:
                        data_baru[key] =  value
                
                # save in client data variable
                dataclient_PILOT[client['callsign']] = data_baru
                
    elif key == "servers":
        # loop over server data
        for server in value:
            dataserver[server['ident']] = server

# convert data to JSON
dataserver = json.dumps(dataserver, sort_keys=True)
dataclient_ATC = json.dumps(dataclient_ATC, sort_keys=True)
dataclient_PILOT = json.dumps(dataclient_PILOT, sort_keys=True)

# save data to a external JSON file
with open("result/server.json", "w+") as f:
    f.write(dataserver)

with open("result/atc.json", "w+") as f:
    f.write(dataclient_ATC)

with open("result/pilot.json", "w+") as f:
    f.write(dataclient_PILOT)