import time
import os

def ping_target(url, ping_interval):
    print(f"Starting Ping Module for {url} with an interval of {ping_interval} seconds...")
    while True:
        response = os.system(f"ping -c 1 {url}" if os.name != "nt" else f"ping -n 1 {url}")
        if response == 0:
            print(f"Ping to {url} succeeded.")
        else:
            print(f"Ping to {url} failed.")
        time.sleep(ping_interval)

if __name__ == "__main__":
    # Read parameters from globals
    url = globals().get("url", "google.com")
    ping_interval = globals().get("ping_interval", 5)

    # Start the ping function
    ping_target(url, ping_interval)
