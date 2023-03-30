import sys
import json

verdict = list(map(lambda x: x.strip(), list(sys.stdin)))

with open('scoring.json') as cat_file:
    data = json.load(cat_file)['scoring']

amount = 0
for elem in data:
    for test in elem['required_tests']:
        if verdict[test - 1] == 'ok':
            amount += elem['points'] / len(elem['required_tests'])

print(int(amount))
