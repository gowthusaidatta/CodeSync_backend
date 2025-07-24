import requests

def get_leetcode_data(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "LeetCode API error"}

    data = response.json()

    if "status" in data and data["status"] == "error":
        return {"error": "User not found"}

    return {
        "platform": "LeetCode",
        "username": username,
        "total_problems_solved": data.get("totalSolved", 0),
        "ranking": data.get("ranking", "N/A"),
        "easy": data.get("easySolved", 0),
        "medium": data.get("mediumSolved", 0),
        "hard": data.get("hardSolved", 0)
    }
