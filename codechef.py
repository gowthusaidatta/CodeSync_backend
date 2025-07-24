import requests
from bs4 import BeautifulSoup

def get_profile_data(username):
    url = f"https://www.codechef.com/users/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = {}

    # Extract Username
    username_tag = soup.find('h1', class_='h2-style')
    data['username'] = username_tag.text.strip() if username_tag else "Not Found"

    # Problems Solved
    problems_solved = "Not Found"
    for h3 in soup.find_all('h3'):
        if 'Total Problems Solved' in h3.text:
            problems_solved = h3.text.strip().split(":")[-1].strip()
            break
    data['problems_solved'] = problems_solved

    # Rating
    rating_div = soup.find('div', class_='rating-number')
    data['contest_rating'] = rating_div.text.strip() if rating_div else "Not Found"

    # Stars
    stars_span = soup.find('span', class_='rating')
    data['stars'] = stars_span.text.strip() if stars_span else "Not Found"

    return data
