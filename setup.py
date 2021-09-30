from setuptools import setup, find_packages

setup(
    name="timechecker1",
    version="1.0.5",
    author="Saksham Gupta",
    author_email="sakshamgupta026@gmail.com",
    description="An aplication that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["timechecker = src.main:main"]},
)
