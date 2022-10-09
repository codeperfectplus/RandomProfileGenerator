'''
python Random Profile generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  

'''
import os
import random
from random_profile.utils import load_txt_file

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

fname_txt = os.path.join(ROOT_DIR, "random_profile/assets/fnames.txt")
lname_txt = os.path.join(ROOT_DIR, "random_profile/assets/lnames.txt")
states_names_txt = os.path.join(ROOT_DIR, "random_profile/assets/street_names.txt")
cities_name_txt = os.path.join(ROOT_DIR, "random_profile/assets/cities_name.txt")
states_names_txt = os.path.join(ROOT_DIR, "random_profile/assets/states_names.txt")

# loading data from txt files
fname = load_txt_file(fname_txt)
lname = load_txt_file(lname_txt)
states_names = load_txt_file(states_names_txt)
cities_name = load_txt_file(cities_name_txt)
street_names = load_txt_file(states_names_txt)

class RandomProfile:
    def __init__(self, num=1):
        '''
        num = Total No. of Name You Want To Print
        deafult is 1
        To Print More Than one Name Change value of num
        '''
        self.num = num

    def first_name(self):
        # print first name
        first_name_list = [random.choice(fname) for _ in range(self.num)]
        return first_name_list

    def last_name(self):
        # print last name
        last_name_list = [random.choice(lname) for _ in range(self.num)]
        return last_name_list

    def full_name(self):
        # print full name
        full_name_list = [random.choice(
            fname) + ' ' + random.choice(lname) for _ in range(self.num)]
        return full_name_list

    def full_profile(self):
        # print full profile
        profile_list = []
        for _ in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            phone = f'+ +1-{random.randint(300, 500)}{random.randint(800, 999)}{random.randint(1000,9999)}'

            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city = random.choice(cities_name)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = f'{street_num} {street} St. {city} {state} {zip_code}'
            email = first.lower() + last.lower() + '@bogusemail.com'

            profile_dict = {}
            profile_dict['first_name'] = first
            profile_dict['last_name'] = last
            profile_dict['phone'] = phone
            profile_dict['address'] = address
            profile_dict['email'] = email
            profile_list.append(profile_dict)

        return profile_list
