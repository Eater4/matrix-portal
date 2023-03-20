import time
import board
import adafruit_requests as requests
import terminalio
import json
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_matrixportal.network import Network

network = Network(status_neopixel=board.NEOPIXEL, debug=True)

SPOTIFY_GET_CURRENT_TRACK_URL = "https://api.spotify.com/v1/me/player/currently-playing"
ACCESS_TOKEN = "BQDiy2hZ9T-VuaGNXzF8zesqRE846dJMMY-Gs5r0pexOBmrcpr1lGJLDHOIHtIq0AZRGLbUoAgvRrzmtGAJaapyKDLvuuIC9Ro4r9DlgPkUdwfXNVgKUu47pabGglrG8BAhVDrIgLQntg045GjL5EXlu-UCXPVdR3vBKQS8N8WYh4ssL"


def get_current_track(access_token):
    response = network.fetch(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    json_resp = response.json()
    track_name = json_resp["item"]["name"]
    artists = [artist for artist in json_resp["item"]["artists"]]
    artist_names = ", ".join([artist["name"] for artist in artists])

    current_track_info = {
        "track_name": track_name,
        "artists": artist_names,
    }

    return current_track_info


def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(ACCESS_TOKEN)
        print(current_track_info)
    time.sleep(1)


if __name__ == "__main__":
    main()
