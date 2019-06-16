import json

def startup():
    with open('json files/employees.json') as json_file:
        data = json.load(json_file)
        for e in data['Employees']:
            print('Name: ' + e['preferredFullName'])
            print('Title: ' + e['jobTitleName'])
            print('Availability: ' + e['availability'])
            print('Hours: ' + e['hours'])
            print('')


startup()

