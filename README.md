# Backloggd Py

A Python script to scrape the currently playing video games from a user's public [Backloggd](https://backloggd.com/) profile.

## Prerequisites

* Install Python 3.x (Installed automatically when installing [Homebrew](https://brew.sh/) on MacOS)
* Install pipenv - `pip install pipenv`
* Install dependencies - `pipenv install`

## Usage
1. Rename `const_example.py` to `const.py`
2. Replace USERNAME in the URL within `const.py` with your Backloggd username
3. Run `pipenv shell` and then `python main.py`