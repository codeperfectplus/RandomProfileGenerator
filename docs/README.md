<h1 align="center">
  <br>
  Random Profile Generator V0.2.3
  <br>
</h1>

<h4 align="center">Python Module To Generate Random Profile Data</h4>

[Random Profile](https://pypi.org/project/random-profile/) is a powerful and simple tool to generate fake data. You can use it to mock classes, populate databases and much more. You can check the full documentation here. Check on [Pypi](https://pypi.org/project/random-profile/)

## Usage

the random-profile module is a random profile generator for many usages like: ex- fake dataset, YouTube videos, content creation, personal projects.

## Installation

- This is A python 3 Package.
- Install python 3.0+ or Anaconda 3.0+

```bash
pip install random-profile   # using pip
conda install random-profile # using anaconda
```

## Documentation

```python
from random_profile import RandomProfile
rp = RandomProfile()
```

### Get first name

```python
rp.first_name(num=10)
```

```bash
['Brooks', 'Ameer', 'Fletcher', 'Amiri', 'Mathew', 'Finnley', 'Raphael', 'Omar', 'Karter', 'Jesiah']
```

### Get full name

```python
# For full name
rp.full_name(num=8)
```

```bash
['Brooks Mccullough', 'Ameer Mccullough', 'Fletcher Mccullough', 'Amiri Mccullough', 'Mathew Mccullough', 'Finnley Mccullough', 'Raphael Mccullough', 'Omar Mccullough']
```

### Get full profile

```python
rp.full_profile(num=1)
```

```bash
[{'first_name': 'Yadiel', 'last_name': 'Morton', 'hair_color': 'brown', 'blood_type': '(AB+)', 'full_name': 'Yadiel Morton', 'DOB': '23/05/2004', 'age': 18, 'height': 143, 'weight': 49, 'phone': '+1-429-996-9609', 'address': '497 Elm St. Springfield WY 73547', 'email': 'yadielmorton@aol.de', 'job_title': 'Game Developer', 'ip_address': '235.8.137.166'}]
```

## License

The project is licensed under the <a href="/LICENSE">MIT</a> license. 

## Contributors

<a href="https://github.com/codePerfectPlus/awesomeScripts/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=codePerfectPlus/randomprofilegenerator" />
</a>
