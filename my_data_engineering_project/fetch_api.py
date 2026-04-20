import requests
import time
from config import API_KEY, BASE_URL


def build_url(endpoint, page=None):
    url = f"{BASE_URL}/{endpoint}?api_key={API_KEY}"
    if page:
        url += f"&page={page}"
    return url


def fetch_page(endpoint, page):
    url = build_url(endpoint, page)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()["results"]
        else:
            print(f"Error {response.status_code} on page {page}")
            return None

    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
        time.sleep(5)
        return None


def fetch_all_pages(endpoint, start=1, end=200):
    all_data = []

    for page in range(start, end + 1):
        print(f"Fetching page {page}...")

        data = fetch_page(endpoint, page)

        if data:
            all_data.extend(data)
        else:
            print("Stopping early due to error")
            break

        time.sleep(0.1)

    return all_data

from data_utils import to_dataframe, save_csv


def fetch_and_save_raw(endpoint, start=1, end=200):
    all_data = fetch_all_pages(endpoint, start, end)

    df = to_dataframe(all_data)

    file_path = f"data/raw/{endpoint}_movies.csv"
    save_csv(df, file_path)

    return df