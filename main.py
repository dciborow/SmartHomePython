# This is a sample Python script.
import json
import yaml

from smarthome.honeywell import get_devices, get_rooms

if __name__ == "__main__":

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
