
from dotenv import load_dotenv
import finnhub
import os

load_dotenv() #load .env

'''
Connect finnhub API
'''
def connectAPI():
    finnhub_client  = finnhub.Client(api_key=os.getenv("API_KEY"))
    return finnhub_client

