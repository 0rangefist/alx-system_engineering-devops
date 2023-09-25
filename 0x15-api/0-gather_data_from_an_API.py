#!/usr/bin/python3
"""
This script fetches response from an API
"""
import requests
import sys


def get_employee_todos(employee_id):
    """
    Returns info about an employee's TODO list progress
    """
    id_endpoint = "https://jsonplaceholder.typicode.com/users/" + employee_id
    todos_endpoint = id_endpoint + "/todos"

    try:
        # Get user's name
        response = requests.get(id_endpoint)
        employee_name = response.json()['name']

        # Get number of tasks done
        response = requests.get(todos_endpoint)
        todos = response.json()

        # Get total number of tasks
        total_tasks = len(todos)

        # Get number of completed tasks
        tasks_completed = 0
        for todo in todos:
            if todo.get('completed'):
                tasks_completed += 1

        # Print out formatted data
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, tasks_completed, total_tasks
        ))
        for todo in todos:
            if todo.get('completed'):
                print("\t " + todo.get('title'))

    except Exception:
        print("Something went wrong.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        exit()

    # check if input is an integer
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Usage: python script.py <employee_id>")
        exit()

    get_employee_todos(employee_id)
