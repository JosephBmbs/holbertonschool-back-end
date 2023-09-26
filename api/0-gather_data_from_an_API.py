#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = '{}users/{}'.format(base_url, employee_id)
    tasks_url = '{}todos?userId={}'.format(base_url, employee_id)

    try:
        employee_info = requests.get(user_url).json()
        tasks_info = requests.get(tasks_url).json()

        employee_name = employee_info.get('name')
        completed_tasks = [task for task in tasks_info if task.get('completed')]
        total_tasks = len(tasks_info)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed_tasks), total_tasks))

        for task in completed_tasks:
            print("\t {}".format(task.get('title')))
    except ValueError:
        print("Not a valid JSON response.")
