import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="random_profile",
    version="1.0.0",
    author="Deepak Raj",
    author_email="deepak008@live.com",
    description="Generate Random Profile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    data_files=[('assets', glob('random_profile/assets/*'))],
    url="https://github.com/codePerfectPlus/Random-Profile-Generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Environment :: Plugins",
        
    ],
    entry_points={
        "console_scripts": ["random_profile = random_profile.__main__:main"],
    },
)
