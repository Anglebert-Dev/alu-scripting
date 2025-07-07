#!/usr/bin/python3
"""Print the titles of the first 10 Hot Posts"""
import requests


def top_ten(subreddit):
    """The top ten titles"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            posts = response.json().get('data', {}).get('children', [])
            for i in range(min(10, len(posts))):
                print(posts[i].get('data', {}).get('title'))
        except Exception:
            print(None)
    else:
        print(None)
