#!/usr/bin/python3
"""Print the titles of the first 10 Hot Posts"""

import requests


def top_ten(subreddit):
    """The top ten titles"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        json_data = response.json()
        try:
            children = json_data.get('data', {}).get('children', [])
            for i in range(min(10, len(children))):
                title = children[i].get('data', {}).get('title')
                if title:
                    print(title)
        except (KeyError, IndexError, TypeError):
            pass
    else:
        print(None)
