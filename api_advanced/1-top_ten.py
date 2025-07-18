#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the top 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Prints the top 10 hot post titles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditScript/1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print(None)
