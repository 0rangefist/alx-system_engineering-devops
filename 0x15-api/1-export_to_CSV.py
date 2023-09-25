#!/usr/bin/python3
"""
This script fetches response from an API and exports data in CSV format
"""
import csv
import requests
import sys


def export_todos_to_csv(employee_id):
    """
    Returns info about an employee's TODO list progress
    """
    id_endpoint = "https://jsonplaceholder.typicode.com/users/" + employee_id
    todos_endpoint = id_endpoint + "/todos"

    try:
        # Get user's data
        response = requests.get(id_endpoint)
        user_data = response.json()
        username = user_data.get('username')

        # Get tasks data
        response = requests.get(todos_endpoint)
        todos = response.json()

        # Create a CSV file
        csv_filename = employee_id + ".csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

            # Write todo rows
            for todo in todos:
                task_completed_status = str(todo.get('completed'))
                task_title = todo.get('title')
                csv_writer.writerow([employee_id, username,
                                    task_completed_status, task_title])

        print("Data has been exported to " + csv_filename)

    except Exception:
        print("Something went wrong.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # check if input is an integer
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    export_todos_to_csv(employee_id)
