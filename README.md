<h1 align="center">
  <br>
  Random Profile Generator V0.2.3
  <br>
</h1>

<h4 align="center">Python Module To Generate Random Profile Data</h4>

<p align="center">
<img src="https://img.shields.io/pypi/v/random-profile.svg">
<img src="https://img.shields.io/pypi/pyversions/random-profile.svg">
<img src="https://img.shields.io/pypi/l/random-profile.svg">
</p>
<p align="center">
<img src="https://img.shields.io/pypi/dd/random-profile.svg">
<img src="https://img.shields.io/pypi/dw/random-profile.svg">
<img src="https://img.shields.io/pypi/dm/random-profile.svg">
</p>

[RandomProfile](https://pypi.org/project/random-profile/) is a powerful and simple tool to generate fake data. You can use it to mock classes, populate databases and and much more. You can check the full documentation here. Check on [Pypi](https://pypi.org/project/random-profile/)

## Installation

- This is A python 3 Package.
- Install python 3.0+ or Anaconda 3.0+

```bash
pip install random-profile   # using pip
conda install random-profile # using anaconda
```

## Documentation

### As Python Module

```python
from random_profile import RandomProfile
rp = RandomProfile(num=5)
'''

num = Total No. of Name You Want To Print
default is 1
change the num value according to your needs.
'''
# num can be overwritten in the function

# For first name
rp.first_name(num=10)

# For full name
rp.full_name(num=8)

# override the num value
rp.full_profile(num=10)

# For last name
rp.last_name(num=6)
```

### As Command Line Tool

```bash
$ random-profile --help
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
$ random-profile -n 10 -f # to get 10 full names
$ random-profile -n 10 -p # to get 10 full profiles
$ random-profile -n 10 -l # to get 10 last names
$ random-profile -n 10 -ip # to get 10 ipv4 addresses
$ random-profile -n 10 -j # to get 10 job titles
```


## Support

Contributors for the Project
[CodePerfectPLus](https://github.com/codePerfectPlus)
...

## Roadmap

what's new in future update

- More Random data will be added to package.
- Variety of Random-Data will increase.

## Changelog

v0.2.3
- Flask app added
- Date of Birth Added
- Age added
- Height and Weight Added
- Blood Group and hair color added
- Job title added
- More email domains added
- Bugs Fixed

v0.2.1
- More variation added to the data
- Test cases added
- Created a separate file for data loadings
- Fixed some bugs

## Contributing

Before submitting a bug, please do the following:

Perform basic troubleshooting steps:

- Make sure you are on the latest version. If you are not on the most recent version, your problem may have been solved already! Upgrading is always the best first step.
- Try older versions. If you are already on the latest release, try rolling back a few minor versions (e.g. if on 1.7, try 1.5 or 1.6) and see if the problem goes away. This will help the devs narrow down when the problem first arose in the commit log.
- Try switching up dependency versions. If the software in question has dependencies (other libraries, etc) try upgrading and downgrading those dependencies as well.

## Authors and acknowledgment

Show your appreciation to those who have contributed to the project.

## License

The project is licensed under the <a href="/LICENSE">MIT</a> license. 

## Contributors

<a href="https://github.com/codePerfectPlus/awesomeScripts/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=codePerfectPlus/randomprofilegenerator" />
</a>
