import json
from scraping.leetcode import get_leetcode_data
from scraping.codechef import get_profile_data as get_codechef_data
from scraping.hackerrank import get_hackerrank_data

def build_response(status_code, body_dict):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body_dict)
    }

def lambda_handler(event, context):
    try:
        params = event.get("queryStringParameters", {})
        if not params:
            return build_response(400, {"error": "Missing query parameters."})

        response = {}

        # LeetCode
        leetcode_username = params.get("leetcode")
        if leetcode_username:
            response["leetcode"] = get_leetcode_data(leetcode_username)

        # CodeChef
        codechef_username = params.get("codechef")
        if codechef_username:
            response["codechef"] = get_codechef_data(codechef_username)

        # HackerRank
        hackerrank_username = params.get("hackerrank")
        if hackerrank_username:
            response["hackerrank"] = get_hackerrank_data(hackerrank_username)

        return build_response(200, response)

    except Exception as e:
        return build_response(500, {"error": str(e)})
