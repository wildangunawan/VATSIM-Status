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

# rating list
rating_code = {
    0:"Inactive",
    1:"OBS",
    2:"S1",
    3:"S2",
    4:"S3",
    5:"C1",
    7:"C3",
    8:"INS",
    10:"INS+",
    11:"Supervisor",
    12:"Administrator"
}

rating_name = {
    0:"Inactive",
    1:"Observer",
    2:"Student",
    3:"Student 2",
    4:"Student 3",
    5:"Controller",
    7:"Senior Controller",
    8:"Instructor",
    10:"Senior Instructor",
    11:"Supervisor",
    12:"Administrator",
}

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
                        # ganti rating ke humanized
                        if key == "rating":
                            data_baru['rating'] = rating_code[value]
                            data_baru['rating_code'] = value
                            data_baru['rating_name'] = rating_name[value]
                        else:
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