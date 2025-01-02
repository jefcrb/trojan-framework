import time
import os

def ping_google():
    print("Starting Google Ping Module...")
    while True:
        response = os.system("ping -c 1 google.com" if os.name != "nt" else "ping -n 1 google.com")
        if response == 0:
            print("Ping to google.com succeeded.")
        else:
            print("Ping to google.com failed.")
        time.sleep(5)

if __name__ == "__main__":
    ping_google()
