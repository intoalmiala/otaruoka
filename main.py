import sys
import get
import send

with open(sys.path[0]+"/token") as f:
    TOKEN = f.readline().strip()

CHAT_ID = "@otaruoka"

def main():
    lunch = get.get_lunch()
    send.send_lunch(TOKEN, CHAT_ID, lunch)

if __name__ == "__main__":
    main()
