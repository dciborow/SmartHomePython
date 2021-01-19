# This is a sample Python script.
import json

from smarthome.honeywell import get_devices, get_rooms

if __name__ == '__main__':
    bearer = "1VwAR1waukxuUjSOE5AgNHr3h2OK"

    api_key = "v4M5vCGGt0F6tMwxwb2ac5UGENegSS4H"
    location_id = "2231065"
    deviceID = "LCC-48A2E6039C30"

    get_devices_response = get_devices(bearer, api_key, location_id)
    print(json.dumps(get_devices_response, indent=3))

    get_rooms_response = get_rooms(bearer, api_key, location_id, deviceID, "0")
    print(json.dumps(get_rooms_response, indent=3))
