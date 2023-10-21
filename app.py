import os
from bardapi import Bard
from dotenv import load_dotenv


load_dotenv()

# CREATE YOUR OWN .ENV FILE AND ASSIGN YOUR COOKIE AS COOKIE_TOKEN
token = os.environ["COOKIE_TOKEN"]

bard = Bard(token=token)

askContent = input("Enter query: ")

response = bard.get_answer(askContent)["content"]

print(response)
