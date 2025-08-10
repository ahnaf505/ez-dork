import os
from osint import *

def main_banner():
	print(r"""

  /$$$$$$           /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$
 /$$__  $$         /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/
| $$  \ $$        | $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$   
| $$$$$$$$ /$$$$$$| $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$   
| $$__  $$|______/| $$  | $$ \____  $$  | $$  | $$  $$$$   | $$   
| $$  | $$        | $$  | $$ /$$  \ $$  | $$  | $$\  $$$   | $$   
| $$  | $$        |  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$   | $$   
|__/  |__/         \______/  \______/ |______/|__/  \__/   |__/   

BY:ahnaf505
""")

def dorks_banner():
	print("[SE DORKING]\n\n")
	print("[INFO] > Input a Full Name, ID, or anything that may be a public piece of information.")
	print("[INFO] > You can input up to 5 variation of keywords, this can inlude different formatting for names.\n")

def error(errorvalue):
	print(f"[ERROR] > {errorvalue}")

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def menu():
	print("""\nLOOKUP
1 > Using Dorks (Google, -Bing-, -DuckDuckGo-)
2 > Using Instagram Username
3 > Using Tiktok Username
		""")

def ai_resultsummary(chatobject):
	reply = chatobject.send(SEARCH_SUMMARY)
	return reply

def askmenu():
	return input("[MENU] > ")

def dorking_input1():
	while True:
		amount = input("[SE DORKING] Amount of keyword to use > ")
		try:
			match int(amount):
				case 1 | 2 | 3 | 4 | 4:
					return amount
				case _:
					error("Invalid Input")
		except ValueError:
			error("Invalid Input")

def dorking_input2(varamount):
	itera = 0
	keywords = []
	while True:
		itera += 1
		keyword = input(f"[SE DORKING] Keyword {itera} > ")
		if keyword != '':
			keywords.append(keyword)
		if itera >= int(varamount):
			return keywords


def processmenu(input):
	match input:
		case "1":
			clear()
			main_banner()
			dorks_banner()
			var = dorking_input1()
			keywords = dorking_input2(var)
			search_summary, chat = google_dorks(keywords)
			resultsum = remove_think(ai_resultsummary(chat))
			print(resultsum)
			return True
		case _:
			error("Invalid menu input")
			return False