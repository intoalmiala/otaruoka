import get_lunch as gl
import send_lunch as sl

with open("token") as f:
    TOKEN = f.readline().strip()

CHAT_ID = "@otaruoka"

def main():
    if lunch := gl.get_lunch():
        sl.send_lunch(TOKEN, CHAT_ID, lunch)
    else:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

if __name__ == "__main__":
    main()
