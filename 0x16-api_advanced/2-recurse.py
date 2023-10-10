#!/usr/bin/python3
"""
This script fetches the titles of the first 10 hot posts for a
given subreddit from the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches and returns a list containing the
    titles of hot articles for a given subreddit.
    """
    # Increased limit for more results
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent header as per Reddit's API guidelines
    headers = {"User-Agent": "Custom User Agent"}

    params = {"after": after} if after else {}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            titles = [post["data"]["title"] for post in posts]
            # Extend the hot_list with titles from the current page
            hot_list.extend(titles)

            # Check if there are more pages (pagination) and
            # continue the recursion
            if "after" in data["data"]:
                after = data["data"]["after"]
                return recurse(subreddit, hot_list, after)
            else:
                # Return the finallist of titles when no more pages
                return hot_list

        else:
            return None  # No posts found

    except requests.exceptions.HTTPError:
        return None  # Invalid subreddit or other HTTP error


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        hot_articles = recurse(subreddit_name)

        if hot_articles:
            print(len(hot_articles))
        else:
            print("None")
