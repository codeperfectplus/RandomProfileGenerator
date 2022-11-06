'''
python Random Profile generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
'''

import os
import uuid
import random
from typing import List, Tuple

from random_profile.utils import ipv4_gen
from random_profile.utils import load_txt_file
from random_profile.utils import generate_dob_age
from random_profile.utils import generate_random_height_weight
from random_profile.utils import ASSETS_DIR

VERSION = "1.0.1"

fname_txt = os.path.join(ASSETS_DIR, "fnames.txt")
lname_txt = os.path.join(ASSETS_DIR, "lnames.txt")
hair_colors_txt = os.path.join(ASSETS_DIR, "hair_colors.txt")
blood_types_txt = os.path.join(ASSETS_DIR, "blood_types.txt")
street_names_txt = os.path.join(ASSETS_DIR, "street_names.txt")
cities_name_txt = os.path.join(ASSETS_DIR, "cities_name.txt")
states_names_txt = os.path.join(ASSETS_DIR, "states_names.txt")
job_titles_txt = os.path.join(ASSETS_DIR, "job_titles.txt")
states_hash_json = os.path.join(ASSETS_DIR, "states_hash.json")

# loading data from txt files
fname = load_txt_file(fname_txt)
lname = load_txt_file(lname_txt)
hair_colors = load_txt_file(hair_colors_txt)
blood_types = load_txt_file(blood_types_txt)
states_names = load_txt_file(states_names_txt)
cities_name = load_txt_file(cities_name_txt)
street_names = load_txt_file(street_names_txt)
job_titles = load_txt_file(job_titles_txt)


class RandomProfile(object):
    """ Random Profile Generator """
    def __init__(self, num: int = 1):
        self.num = num

    def __str__(self) -> str:
        return f"Random Profile Generator version {VERSION}"

    def __repr__(self) -> str:
        return f"RandomProfile(num={self.num})"

    def __call__(self, num: int = None) -> List[dict]:
        return self.full_profile(num)

    def __iter__(self):
        yield self.full_profile()

    def __next__(self):
        yield self.full_profile()

    def __len__(self):
        return self.num

    def __getitem__(self, index):
        return self.full_profile()[index]

    def first_name(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return random.choices(fname, k=num)

    def last_name(self, num: int = None) -> list:
        num = self.num if num is None else num
        return random.choices(lname, k=num)

    def full_name(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return [random.choice(fname) + ' ' + random.choice(lname) for _ in range(num)]

    def ip_address(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return [ipv4_gen() for _ in range(num)]

    def job_title(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return random.choices(job_titles, k=num)

    def blood_type(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return random.choices(blood_types, k=num)

    def hair_color(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return random.choices(hair_colors, k=num)

    def dob_age(self, num: int = None) -> List[Tuple[str, int]]:
        num = self.num if num is None else num
        return [generate_dob_age() for _ in range(num)]

    def height_weight(self, num: int = None) -> List[Tuple[int, int]]:
        num = self.num if num is None else num
        return [generate_random_height_weight() for _ in range(num)]

    def city(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return random.choices(cities_name, k=num)

    def phone_number(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return [f'+1{random.randint(1000000000, 9999999999)}' for _ in range(num)]

    def postal_code(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return [str(random.randint(10000, 99999)) for _ in range(num)]

    def state(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        return random.choices(states_names, k=num)

    def generate_address(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        address_list = []
        for _ in range(num):
            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city = random.choice(cities_name)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = f'{street_num}, {street}, {city} {zip_code} {state}, USA'
            address_list.append(address)

        return address_list

    def full_profile(self, num: int = None) -> List[dict]:
        num = self.num if num is None else num
        profile_list = []
        for _ in range(num):
            unique_id = str(uuid.uuid4())

            first = random.choice(fname)
            last = random.choice(lname)
            full_name = first + ' ' + last

            job_title = random.choice(job_titles)
            dob, age = generate_dob_age()

            phone = f'+1-{random.randint(300, 500)}-{random.randint(800, 999)}-{random.randint(1000,9999)}'
            email = first.lower() + last.lower() + '@example.com'

            blood_type = random.choice(blood_types)
            height, weight = generate_random_height_weight()
            hair_color = random.choice(hair_colors)
            ip_address = ipv4_gen()

            profile_dict = {}
            profile_dict['id'] = unique_id
            profile_dict['first_name'] = first
            profile_dict['last_name'] = last
            profile_dict['full_name'] = full_name
            profile_dict['job_title'] = job_title
            profile_dict['dob'] = dob
            profile_dict['age'] = age
            profile_dict['phone_number'] = phone
            profile_dict['email'] = email
            profile_dict['address'] = self.generate_address()[0]
            profile_dict['blood_type'] = blood_type
            profile_dict['height'] = height
            profile_dict['weight'] = weight
            profile_dict['hair_color'] = hair_color
            profile_dict['ip_address'] = ip_address

            profile_list.append(profile_dict)

        return profile_list
