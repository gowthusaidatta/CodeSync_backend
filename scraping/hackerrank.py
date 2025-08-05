# scraping/hackerrank.py

import requests
from bs4 import BeautifulSoup

def get_hackerrank_data(username):
    try:
        url = f"https://www.hackerrank.com/{username}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"User '{username}' not found or profile is private."}

        soup = BeautifulSoup(response.text, "html.parser")

        # You can update these based on real DOM structure of HackerRank
        badges = soup.find_all("div", class_="hacker-badge")  # just an example
        badge_count = len(badges)

        return {
            "platform": "HackerRank",
            "username": username,
            "badges": badge_count,
        }

    except Exception as e:
        return {"error": str(e)}
