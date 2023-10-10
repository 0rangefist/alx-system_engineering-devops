#!/usr/bin/python3
"""
This script fetches the titles of the first 10 hot posts for a
given subreddit from the Reddit API.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts for the given subreddit.
    """
    endpoint = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit)

    # Set a custom User-Agent header to prevent rate limiting
    # error as per Reddit's API guidelines.
    http_headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(endpoint,
                            headers=http_headers,
                            allow_redirects=False)
    if response.status_code >= 300:
        print(None)
    else:
        [print(post.get("data").get("title"))
         for post in response.json().get("data").get("children")]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
