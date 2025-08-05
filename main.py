from fastapi import FastAPI
from scraping.leetcode import get_leetcode_data
from scraping.codechef import get_profile_data as get_codechef_data
from scraping.hackerrank import get_hackerrank_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "✅ CodeSync backend running on Railway!"}

@app.get("/get-score")
def get_score(leetcode: str = None, codechef: str = None, hackerrank: str = None):
    if not any([leetcode, codechef, hackerrank]):
        return {"error": "❌ Missing query parameters."}
    
    response = {}
    if leetcode:
        response["leetcode"] = get_leetcode_data(leetcode)
    if codechef:
        response["codechef"] = get_codechef_data(codechef)
    if hackerrank:
        response["hackerrank"] = get_hackerrank_data(hackerrank)

    return response
