'''
python random name generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
'''
import random
first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria','Adam','Sturt','Nikolson','Tom','Harry','Ruskin']
last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin','Potter']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

first = random.choice(first_names)
last = random.choice(last_names)

phone = f'+91-{random.randint(800, 999)}{random.randint(800, 999)}{random.randint(1000,9999)}'

street_num = random.randint(100, 999)
street = random.choice(street_names)
city = random.choice(fake_cities)
state = random.choice(states)
zip_code = random.randint(10000, 99999)
address = f'{street_num} {street} St., {city} {state} {zip_code}'
email = first.lower() + last.lower() + '@bogusemail.com'

class Name:
    def __init__(self,num=1):
        '''
        num = Total No. of Name You Want
        ''' 
        self.num = num

    def first_name(self):
        for i in range(self.num):
            print(f'{first}')

    def last_name(self):
        for i in range(self.num):
            print(f'{last}')
   
    def full_name(self):
        for i in range(self.num):
            print(f'{first} {last}')

    def full_profile(self):
        for i in range(self.num):
            print(f'{first} {last} \n {street_num}-{street} {city}-{state}\n{zip_code}\n{phone}\n{email}')

