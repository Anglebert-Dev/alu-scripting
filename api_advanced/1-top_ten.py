#!/usr/bin/python3
"""Print the titles of the first 10 hot posts from a subreddit"""
import requests


def top_ten(subreddit):
    """The top ten titles"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    json_data = response.json()
    posts = json_data.get('data', {}).get('children', [])

    if not posts:
        print("None")
        return

    for post in posts:
        title = post.get('data', {}).get('title')
        if title:
            print(title)
