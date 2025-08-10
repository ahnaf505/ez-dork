from browser import *
from ai import *
from prompt import *

API_KEY = "fw_3ZTzXKyN8ywwipNSQjkBW4mP"

def google(keyword, rawword, chatobject):
	rawResult = getAllVisibleText(f"https://www.google.com/search?udm=14&q={keyword}")
	reply = chatobject.send(prompt(INITIAL_SEARCHRESULT, {"keyword":rawword, "blob":rawResult}))
	return reply

def google_dorks(keywords):
    MODEL = "qwen3-30b-a3b"
    chat = LLMChatSession(model=MODEL, api_key=API_KEY)
    rawSorted = []
    for keyword in keywords:
    	quoted = google(f'"{keyword}"', keyword, chat)
    	rawSorted.append(quoted)
    	intext = google(f'intext:"{keyword}"', keyword, chat)
    	rawSorted.append(intext)
    	standard = google(keyword, keyword, chat)
    	rawSorted.append(standard)
    	archive = google(f'site:archive.org "{keyword}"', keyword, chat)
    	rawSorted.append(archive)
    	standard = google(f'site:gov "{keyword}"', keyword, chat)
    	rawSorted.append(standard)

    return rawSorted, chat


