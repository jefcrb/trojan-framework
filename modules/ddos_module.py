import time
import os

def ping_target(url, ping_interval):
    print(f"begin ping module naar {url} met interval van {ping_interval} seconden...")
    while True:
        response = os.system(f"ping -c 1 {url}" if os.name != "nt" else f"ping -n 1 {url}")
        if response == 0:
            print(f"ping naar {url} succesvol")
        else:
            print(f"ping naar {url} gefaald")
        time.sleep(ping_interval)

if __name__ == "__main__":
    url = "google.com" # default
    ping_interval = 5

    try:
        url = globals().get("url", url)
        ping_interval = globals().get("ping_interval", ping_interval)
    except Exception as e:
        print(f"Error: {e}")

    ping_target(url, ping_interval)
