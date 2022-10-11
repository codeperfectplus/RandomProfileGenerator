import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Here is the module name.
    name="random_profile",
    # version of the module
    version="0.1.0",
    # Name of Author
    author="CodePerfectPlus",
    # your Email address
    author_email="deepak008@live.com",
    # Small Description about module
    description="Generate Random Profile",
    long_description=long_description,
    # Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
    # Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/codePerfectPlus/Random-Profile-Generator",
    packages=setuptools.find_packages(),
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["random_profile = random_profile.__main__:main"],
    },
)
