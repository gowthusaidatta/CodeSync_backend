import json
from scraping.leetcode import get_leetcode_data
from scraping.codechef import get_profile_data as get_codechef_data
from scraping.hackerrank import get_hackerrank_data

def lambda_handler(event, context):
    print("Event received:", event)

    query = event.get("queryStringParameters") or {}

    leetcode_username = query.get("leetcode")
    codechef_username = query.get("codechef")
    hackerrank_username = query.get("hackerrank")

    if not any([leetcode_username, codechef_username, hackerrank_username]):
        return build_response(400, {"error": "At least one platform username is required"})

    results = {}

    # Fetch from LeetCode
    if leetcode_username:
        try:
            leetcode_data = get_leetcode_data(leetcode_username)
            print("✅ LeetCode Response:", leetcode_data)
            results["leetcode"] = leetcode_data
        except Exception as e:
            print("❌ LeetCode Error:", str(e))
            results["leetcode"] = {"error": str(e)}

    # Fetch from CodeChef
    if codechef_username:
        try:
            codechef_data = get_codechef_data(codechef_username)
            print("✅ CodeChef Response:", codechef_data)
            results["codechef"] = codechef_data
        except Exception as e:
            print("❌ CodeChef Error:", str(e))
            results["codechef"] = {"error": str(e)}

    # Fetch from HackerRank
    if hackerrank_username:
        try:
            hackerrank_data = get_hackerrank_data(hackerrank_username)
            print("✅ HackerRank Response:", hackerrank_data)
            results["hackerrank"] = hackerrank_data
        except Exception as e:
            print("❌ HackerRank Error:", str(e))
            results["hackerrank"] = {"error": str(e)}

    return build_response(200, results)

# ✅ Helper function to wrap response with CORS & JSON headers
def build_response(status_code, body_dict):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body_dict)
    }
