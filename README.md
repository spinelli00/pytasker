## PYTASKER 

A task manager written in python, running in CLI !  

## Features

-  Add, view, and manage tasks
-  Set priorities and status (pending, done)
-  Save and load data in JSON
-  Generate task reports and filters
-  Export to CSV (optional)
-  Multiple user support (planned)

## Technologies

- Python 3.x
- Standard libraries only: `json`, `datetime`, etc.

## Project Structure 

pytasker/
│
├── main.py # CLI interface
├── tasks.py # Task class
├── user.py # User class
├── storage.py # Load/save tasks
├── utils.py # Helper functions
└── data/
├── tasksstorage.json
└── usersstorage.json

## How to Run

git clone https://github.com/spinelli00/pytasker.git

cd pytasker

python main.py