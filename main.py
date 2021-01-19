# This is a sample Python script.
import json
import yaml

from smarthome.honeywell import get_devices, get_rooms

if __name__ == "__main__":
    bearer = "1VwAR1waukxuUjSOE5AgNHr3h2OK"

    api_key = "v4M5vCGGt0F6tMwxwb2ac5UGENegSS4H"
    location_id = "2231065"
    deviceID = "LCC-48A2E6039C30"

    with open("config.yaml") as f:
        # use safe_load instead load
        config = yaml.safe_load(f)

        get_devices_response = get_devices(
            config["bearer"], config["api_key"], config["location_id"]
        )
        print(json.dumps(get_devices_response, indent=3))

        get_rooms_response = get_rooms(
            config["bearer"],
            config["api_key"],
            config["location_id"],
            config["deviceID"],
            "0",
        )
        print(json.dumps(get_rooms_response, indent=3))
