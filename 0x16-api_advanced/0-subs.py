#!/usr/bin/python3
"""
This script fetches a response from the reddit API
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"

    # set custom User-Agent header to prevent rate limiting error
    # per Reddit's API guidelines
    http_headers = {"User-Agent": "Custom User Agent"}

    try:
        response = requests.get(endpoint, headers=http_headers)
        response.raise_for_status()  # raise exception if error status
        json_data = response.json()
        return json_data["data"]["subscribers"]
    except requests.exceptions.HTTPError:
        return 0  # invalid subreddit

    # if response.status_code == 200:
    #     data = response.json()
    #     subscribers = data["data"]["subscribers"]
    #     return subscribers
    # else:
    #     return 0  # invalid subreddit


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a subreddit to search")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
