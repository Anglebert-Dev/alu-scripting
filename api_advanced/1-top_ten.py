#!/usr/bin/python3
"""Print the titles of the first 10 hot posts from a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit"""
    # Check if subreddit is valid (not None or empty)
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(None)
            return
        
        # Parse JSON response
        json_data = response.json()
        
        # Check if the response has the expected structure
        if 'data' not in json_data or 'children' not in json_data['data']:
            print(None)
            return
        
        posts = json_data['data']['children']
        
        # Check if we have posts
        if not posts:
            print(None)
            return
        
        # Print titles of the first 10 posts
        for post in posts[:10]:  # Ensure we only get 10 posts
            post_data = post.get('data', {})
            title = post_data.get('title')
            if title:
                print(title)
    
    except (requests.exceptions.RequestException, ValueError, KeyError):
        print(None)
