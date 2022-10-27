<h1 align="center">
  <br>
  Random Profile Generator V0.2.3
  <br>
</h1>

<h4 align="center">Python Module To Generate Random Profile Data</h4>

[Random Profile](https://pypi.org/project/random-profile/) is a powerful and simple tool to generate fake data. You can use it to mock classes, populate databases and much more. You can check the full documentation here. Check on [Pypi](https://pypi.org/project/random-profile/)


## Installation

- This is A python 3 Package.
- Install python 3.0+ or Anaconda 3.0+

```bash
pip install random-profile   # using pip
conda install random-profile # using anaconda
```

## As Module

```python
from random_profile import RandomProfile
rp = RandomProfile()
```

### Get First Name

```python
rp.first_name(num=10)
```

```bash
['Brooks', 'Ameer', 'Fletcher', 'Amiri', 'Mathew', 'Finnley', 'Raphael', 'Omar', 'Karter', 'Jesiah']
```

### Get Full Name

```python
# For full name
rp.full_name(num=8)
```

```bash
['Brooks Mccullough', 'Ameer Mccullough', 'Fletcher Mccullough', 'Amiri Mccullough', 'Mathew Mccullough', 'Finnley Mccullough', 'Raphael Mccullough', 'Omar Mccullough']
```

### Get Full Profile

```python
rp.full_profile(num=1)
```

```bash
[{'first_name': 'Yadiel', 'last_name': 'Morton', 'hair_color': 'brown', 'blood_type': '(AB+)', 'full_name': 'Yadiel Morton', 'DOB': '23/05/2004', 'age': 18, 'height': 143, 'weight': 49, 'phone': '+1-429-996-9609', 'address': '497 Elm St. Springfield WY 73547', 'email': 'yadielmorton@aol.de', 'job_title': 'Game Developer', 'ip_address': '235.8.137.166'}]
```

## As Command Line Tool

```bash
random-profile --help
Usage: random-profile [OPTIONS]

usage: random_profile [-h] [-n N] [-f | -p | -l | -ip | -j]

optional arguments:
  -h, --help      show this help message and exit
  -n N            Number of random profiles
  -f, --fullname  Get full name instead of first name
  -p, --profile   Get full profile instead of first name
  -l, --lastname  Get last name instead of first name
  -ip, --ipv4     Get an ipv4 IP address
  -j, --jobtitle  Get job title
```

```bash
random-profile -n 10 -f # to get 10 full names
random-profile -n 10 -p # to get 10 full profiles
random-profile -n 10 -l # to get 10 last names
random-profile -n 10 -ip # to get 10 ipv4 addresses
random-profile -n 10 -j # to get 10 job titles
```

## License

The project is licensed under the <a href="/LICENSE">MIT</a> license. 

## Contributors

<a href="https://github.com/codePerfectPlus/awesomeScripts/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=codePerfectPlus/randomprofilegenerator" />
</a>
