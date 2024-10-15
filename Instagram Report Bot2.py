import time
from webbot import Browser
import pyautogui
import argparse
import sys

# To parse the arguments
def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--username", type=str, default="", help="Username to report.")
    parser.add_argument("-f", "--file", type=str, default="acc.txt", help="Accounts list ( Defaults to acc.txt in program directory ).")

    options = parser.parse_args(args)
    return options


def load_accounts(file_path):
    try:
        with open(file_path, "r") as f:
            accounts = [line.strip().split(":") for line in f.readlines()]
        return accounts
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


args = getOptions()

username = args.username
acc_file = args.file

if username == "":
    username = input("Username: ")

accounts = load_accounts(acc_file)

user = []
passw = []

for account in accounts:
    if len(account) == 2:  # Ensure there are both username and password
        user.append(account[0])
        passw.append(account[1])
    else:
        print(f"Invalid entry in accounts file: {account}")

for line in range(len(user)):  # Change to len(user) since it matches the number of valid accounts
    web = Browser()
    web.go_to("https://www.instagram.com/accounts/login/")

    web.type(user[line], into='Phone number, username, or email')
    time.sleep(0.5)
    web.press(web.Key.TAB)
    time.sleep(0.5)
    web.type(passw[line], into='Password')
    web.press(web.Key.ENTER)

    time.sleep(2.0)

    web.go_to(f"https://www.instagram.com/{username}/")

    time.sleep(1.5)

    web.click(xpath='//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')

    time.sleep(0.5)

    web.click(text='Report User')

    time.sleep(1.5)

    web.click(xpath="/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]")

    time.sleep(0.5)

    web.click(text='Close')

    time.sleep(0.5)

    web.click(xpath='/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')

    time.sleep(0.5)

    web.click(xpath='/html/body/div[1]/section/main/div/header/section/div[1]/div/button')

    time.sleep(0.5)

    web.click(text='Log Out')

    time.sleep(0.5)

    pyautogui.keyDown('ctrl')
    time.sleep(0.25)
    pyautogui.keyDown('w')
    time.sleep(0.5)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('w')
