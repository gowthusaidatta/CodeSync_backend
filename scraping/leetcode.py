import requests

def get_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/"
    }
    query = {
        "query": """
        query getUserProfile($username: String!) {
          allQuestionsCount {
            difficulty
            count
          }
          matchedUser(username: $username) {
            username
            submitStats {
              acSubmissionNum {
                difficulty
                count
              }
            }
          }
        }
        """,
        "variables": {
            "username": username
        }
    }

    res = requests.post(url, json=query, headers=headers)

    if res.status_code != 200:
        return {
            "problems_solved": "N/A",
            "Easy": 0,
            "Medium": 0,
            "Hard": 0
        }

    data = res.json()

    matched_user = data.get("data", {}).get("matchedUser")
    if not matched_user:
        return {
            "problems_solved": "N/A",
            "Easy": 0,
            "Medium": 0,
            "Hard": 0
        }

    submissions = matched_user["submitStats"]["acSubmissionNum"]

    easy = next((item["count"] for item in submissions if item["difficulty"] == "Easy"), 0)
    medium = next((item["count"] for item in submissions if item["difficulty"] == "Medium"), 0)
    hard = next((item["count"] for item in submissions if item["difficulty"] == "Hard"), 0)

    return {
        "problems_solved": easy + medium + hard,
        "Easy": easy,
        "Medium": medium,
        "Hard": hard
    }
