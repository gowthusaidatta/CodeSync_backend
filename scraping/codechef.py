import requests
from bs4 import BeautifulSoup

def get_profile_data(username):
    url = f"https://www.codechef.com/users/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    username_tag = soup.find('h1', class_='h2-style')
    username_text = username_tag.text.strip() if username_tag else "Not Found"

    problems_solved = "Not Found"
    h3_tags = soup.find_all('h3')
    for h3 in h3_tags:
        if 'Total Problems Solved' in h3.text:
            problems_solved = h3.text.strip().split(":")[-1].strip()
            break

    rating_div = soup.find('div', class_='rating-number')
    rating = rating_div.text.strip() if rating_div else "Not Found"

    contest_count = soup.find('div', class_='contest-participated-count')
    participated = contest_count.text.strip().split(":")[-1].strip() if contest_count else "Not Found"

    stars_span = soup.find('span', class_='rating')
    stars = stars_span.text.strip() if stars_span else "Not Found"

    return {
        "username": username_text,
        "problems_solved": problems_solved,
        "contest_rating": rating,
        "contests_participated": participated,
        "stars": stars
    }
