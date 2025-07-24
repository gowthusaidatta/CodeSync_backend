import json, requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    username = event.get("queryStringParameters", {}).get("username")
    if not username:
        return response(400, {"error": "Missing username"})

    r = requests.get(f"https://auth.geeksforgeeks.org/user/{username}/practice/",
                     headers={"User-Agent": "Mozilla/5.0"})
    if r.status_code != 200:
        return response(404, {"error": "Profile Not Found"})

    soup = BeautifulSoup(r.content, "html.parser")
    script = soup.find("script", id="__NEXT_DATA__")
    if not script:
        return response(500, {"error": "Unable to locate user data"})

    data = json.loads(script.string)
    page = data.get("props", {}).get("pageProps", {})
    user_info = page.get("userInfo", {})
    subs = page.get("userSubmissionsInfo", {})

    # DEBUG
    print("DEBUG subs.keys():", subs.keys())

    easy = medium = hard = 0
    for k, v in subs.items():
        count = len(v or {})
        key = k.lower()
        if key == "easy":
            easy = count
        elif key == "medium":
            medium = count
        elif key == "hard":
            hard = count

    result = {
        "username": username,
        "fullName": user_info.get("name", ""),
        "profileImage": user_info.get("profile_image_url", ""),
        "institute": user_info.get("institute_name", ""),
        "instituteRank": user_info.get("institute_rank", ""),
        "codingScore": user_info.get("score", 0),
        "monthlyScore": user_info.get("monthly_score", 0),
        "totalProblemsSolved": user_info.get("total_problems_solved", 0),
        "currentStreak": user_info.get("pod_solved_longest_streak", "0"),
        "maxStreak": user_info.get("pod_solved_global_longest_streak", "0"),
        "easyProblems": easy,
        "mediumProblems": medium,
        "hardProblems": hard
    }

    return response(200, result)

def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
