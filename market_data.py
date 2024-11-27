import json
import os
import sqlite3

from dotenv import load_dotenv
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

load_dotenv()

KEY = os.getenv("COINMARKETCAP_API")
DEBUG = True

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": KEY,
}
session = Session()
session.headers.update(headers)


def build_url(path):
    TEST_API_ENDPOINT = "https://sandbox-api.coinmarketcap.com"
    API_ENDPOINT = "https://pro-api.coinmarketcap.com"
    return f"{TEST_API_ENDPOINT}/{path}" if DEBUG else f"{API_ENDPOINT}/{path}"


def get_coins(minimum_threshold, max_threshold):
    parameters = {
        "start": "1",
        "limit": "5000",
        "convert": "USD",
        "market_cap_min": minimum_threshold,
        "market_cap_max": max_threshold,
    }
    url = build_url("v1/cryptocurrency/listings/latest")
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return data


data = get_coins(minimum_threshold=10000000, max_threshold=100000000)
