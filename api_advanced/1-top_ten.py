#!/usr/bin/python3
"""Print the titles of the first 10 hot posts from a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""
    if not subreddit:
        print(None)
        return
    
    headers = {'User-Agent': 'MyRedditApp/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json()
        
        # Check if valid subreddit response (has expected structure)
        if 'data' not in data or 'children' not in data['data']:
            print(None)
            return
        
        posts = data['data']['children']
        
        if not posts:
            print(None)
            return
        
        # Print titles of up to 10 posts
        for post in posts:
            title = post['data']['title']
            print(title)
    
    except Exception:
        print(None)