#!/usr/bin/python3
"""
This script fetches response from an API and exports data in json format
"""
import json
import requests
import sys


def export_all_todos_to_json():
    """
    Returns all employee's TODO list progress
    """
    users_endpoint = "https://jsonplaceholder.typicode.com/users"
    todos_endpoint = "https://jsonplaceholder.typicode.com/todos"

    try:
        # Get all user's data
        response = requests.get(users_endpoint)
        all_users = response.json()

        # Get all todo data
        response = requests.get(todos_endpoint)
        todos = response.json()

        all_employees_todos_dict = {}

        for user in all_users:
            # Create a list to store user data
            todos_list = []
            # Get the user's username
            username = user.get("username")
            # Populate the dictionary
            for todo in todos:
                if todo.get('userId') == user.get('id'):
                    task_completed_status = todo.get('completed')
                    task_title = todo.get('title')
                    todos_list.append({
                        "username": username,
                        "task": task_title,
                        "completed": task_completed_status
                    })
            # Add the user's todo data to all_employees_todos_dict
            all_employees_todos_dict[user.get('id')] = todos_list

        # Export data to JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(all_employees_todos_dict, json_file)

    except Exception:
        print("Something went wrong.")


if __name__ == "__main__":
    export_all_todos_to_json()
