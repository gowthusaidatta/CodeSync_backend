import json
from scraping.leetcode import get_leetcode_data
from scraping.gfg import get_gfg_data
from scraping.codechef import get_codechef_data
from scraping.hackerrank import get_hackerrank_data

def lambda_handler(event, context):
    query = event.get("queryStringParameters") or {}
    platform = query.get("platform", "").lower()
    username = query.get("username")

    if not username or not platform:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing platform or username"})
        }

    if platform == "leetcode":
        data = get_leetcode_data(username)
    elif platform == "gfg":
        data = get_gfg_data(username)
    elif platform == "codechef":
        data = get_codechef_data(username)
    elif platform == "hackerrank":
        data = get_hackerrank_data(username)
    else:
        data = {"error": "Unsupported platform"}

    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }
