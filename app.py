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
server = {}
facilities = {}

# atc
atc = {}
atc_rating = {}

# pilot
pilot = {}
pilot_rating = {}

# store data
# server
for s in data['servers']:
    server[s['ident']] = {
        "name": s['name'],
        "hostname": s['hostname_or_ip'],
        "location": s['location']
    }

# facilities
for f in data['facilities']:
    facilities[f['id']] = {
        "short": f['short'],
        "long": f['long']
    }

# atc rating
for r in data['ratings']:
    atc_rating[r['id']] = {
        "short": r['short'],
        "long": r['long']
    }

# pilot rating
for r in data['pilot_ratings']:
    pilot_rating[r['id']] = {
        "short": r['short_name'],
        "long": r['long_name']
    }

# atc
for a in data['controllers']:
    if a['text_atis'] != None:
        text_atis = "\n".join(list(a['text_atis']))

    atc[a['callsign']] = {
        "cid": a['cid'],
        "name": a['name'],
        "frequency": a['frequency'],
        "rating": f"{atc_rating[a['rating']]['long']} {atc_rating[a['rating']]['short']}",
        "facilities": f"{facilities[a['facility']]['long']} {facilities[a['facility']]['short']}",
        "visual_range": a['visual_range'],
        "atis": text_atis
    }

# pilot
for p in data['pilots']:
    pilot[p['callsign']] = {
        "cid": p['cid'],
        "name": p['name'],
        "rating": f"{pilot_rating[p['pilot_rating']]['long']} {pilot_rating[p['pilot_rating']]['short']}",
        "current_latitude": p['latitude'],
        "current_longitude": p['longitude'],
        "current_altitude": p['altitude'],
        "current_groundspeed": p['groundspeed'],
        "current_transponder": p['transponder'],
    }

    # have flight plan?
    if p['flight_plan'] != None:
        fpl = {
            "flight_rules": "IFR" if p['flight_plan']['flight_rules'] == "I" else "VFR",
            "planned_aircraft": p['flight_plan']['aircraft'],
            "planned_departure": p['flight_plan']['departure'],
            "planned_arrival": p['flight_plan']['arrival'],
            "planned_alternate": p['flight_plan']['alternate'],
            "planned_route": p['flight_plan']['route'],
            "planned_altitude": p['flight_plan']['altitude'],
            "planned_deptime": p['flight_plan']['deptime'],
            "planned_enroute": p['flight_plan']['enroute_time'],
            "remarks": p['flight_plan']['remarks']
        }

        pilot[p['callsign']].update(fpl)

# convert data to JSON
server = json.dumps(server, sort_keys=True)
atc = json.dumps(atc, sort_keys=True)
pilot = json.dumps(pilot, sort_keys=True)

# save data to a external JSON file
with open("result/server.json", "w+") as f:
    f.write(server)

with open("result/atc.json", "w+") as f:
    f.write(atc)

with open("result/pilot.json", "w+") as f:
    f.write(pilot)