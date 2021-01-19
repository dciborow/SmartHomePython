import json

import requests


def get_devices(bearer, api_key, location_id):
    """
    Return all devices in a particular locationID.

    https://developer.honeywellhome.com/lyric/apis/get/devices

    curl \
        -X GET \
        --header "Authorization: Bearer 1VwAR1waukxuUjSOE5AgNHr3h2OK" \
        "https://api.honeywell.com/v2/devices?apikey=v4M5vCGGt0F6tMwxwb2ac5UGENegSS4H&locationId=2231065"
    """
    params = {
        "apikey": api_key,
        "locationId": location_id
    }

    response = requests.get(BASE_URL + "devices", params=params, headers={"Authorization": "Bearer " + bearer})
    if response.status_code != 200:
        raise BaseException

    return json.loads(response.content.decode())


def get_rooms(bearer, api_key, location_id, deviceId, groupId):
    params = {
        "apikey": api_key,
        "locationId": location_id
    }

    response = requests.get(BASE_URL + "devices/thermostats/" + deviceId + "/group/" + groupId + "/rooms",
                            params=params, headers={"Authorization": "Bearer " + bearer})
    if response.status_code != 200:
        raise BaseException(response.status_code)

    return json.loads(response.content.decode())


BASE_URL = "https://api.honeywell.com/v2/"