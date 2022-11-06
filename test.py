from random_profile.utils import load_json

data = load_json(r'random_profile\assets\states_hash.json')

print(data.values())

with open(r'C:\Users\dr\Documents\programming\RandomProfileGenerator\random_profile\assets\states_names.txt', 'w') as fp:
    for state in data.values():
        fp.write(state + '\n')
    