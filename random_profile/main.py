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
import uuid
import random

from random_profile.utils import ipv4_gen
from random_profile.utils import load_txt_file
from random_profile.utils import generate_dob_age
from random_profile.utils import generate_random_height_weight
from random_profile.utils import ROOT_DIR

ASSETS_DIR = os.path.join(ROOT_DIR, "random_profile", "assets")

fname_txt = os.path.join(ASSETS_DIR, "fnames.txt")
lname_txt = os.path.join(ASSETS_DIR, "lnames.txt")
hair_colors_txt = os.path.join(ASSETS_DIR, "hair_colors.txt")
blood_types_txt = os.path.join(ASSETS_DIR, "blood_types.txt")
street_names_txt = os.path.join(ASSETS_DIR, "street_names.txt")
cities_name_txt = os.path.join(ASSETS_DIR, "cities_name.txt")
states_names_txt = os.path.join(ASSETS_DIR, "states_names.txt")
job_titles_txt = os.path.join(ASSETS_DIR, "job_titles.txt")

# loading data from txt files
fname = load_txt_file(fname_txt)
lname = load_txt_file(lname_txt)
hair_colors = load_txt_file(hair_colors_txt)
blood_types = load_txt_file(blood_types_txt)
states_names = load_txt_file(states_names_txt)
cities_name = load_txt_file(cities_name_txt)
street_names = load_txt_file(street_names_txt)
job_titles = load_txt_file(job_titles_txt)

class RandomProfile:
    def __init__(self, num=1):
        '''
        num = Total No. of Name You Want To Print
        default is 1
        To Print More Than one Name Change value of num
        '''
        self.num = num

    def first_name(self, num=None):
        if num is None:
            num = self.num
        first_name_list = [random.choice(fname) for _ in range(num)]
        return first_name_list

    def last_name(self, num=None):
        if num is None:
            num = self.num
        last_name_list = [random.choice(lname) for _ in range(num)]
        return last_name_list

    def full_name(self, num=None):
        if num is None:
            num = self.num
        full_name_list = [random.choice(
            fname) + ' ' + random.choice(lname) for _ in range(num)]
        return full_name_list

    def full_profile(self, num=None):
        if num is None:
            num = self.num
        profile_list = []
        for _ in range(num):
            unique_id = uuid.uuid4().hex
            first = random.choice(fname)
            last = random.choice(lname)
            hair_color = random.choice(hair_colors)
            blood_type = random.choice(blood_types)
            full_name = first + ' ' + last
            phone = f'+1-{random.randint(300, 500)}-{random.randint(800, 999)}-{random.randint(1000,9999)}'
            job_title = random.choice(job_titles)
            ip_address = ipv4_gen()
            email_domain = random.choice(email_domains)
            
            dob, age = generate_dob_age()
            height, weight = generate_random_height_weight()

            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city = random.choice(cities_name)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = f'{street_num} {street} St. {city} {state} {zip_code}'
            email = first.lower() + last.lower() + '@example.com'

            profile_dict = {}
            profile_dict['id'] = unique_id
            profile_dict['first_name'] = first
            profile_dict['last_name'] = last
            profile_dict['hair_color'] = hair_color
            profile_dict['blood_type'] = blood_type
            profile_dict['full_name'] = full_name
            profile_dict['DOB'] = dob
            profile_dict['age'] = age
            profile_dict['height'] = height
            profile_dict['weight'] = weight
            profile_dict['phone'] = phone
            profile_dict['address'] = address
            profile_dict['email'] = email
            profile_dict['job_title'] = job_title
            profile_dict['ip_address'] = ip_address
            profile_list.append(profile_dict)

        return profile_list

    def ipv4(self):
        ip_list = [ipv4_gen() for _ in range(self.num)]
        return ip_list
    
    def job_title(self):
        job_title_list = [random.choice(job_titles) for _ in range(self.num)]
        return job_title_list