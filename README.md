# The Mandrill API using FASTAPI, SQLAlchemy, and SQLite db

This application is designed to fetch response data from the mandrill API asynchronously.

## To install the application

1. Create a local copy of the repository by running
   - '$ git clone https://github.com/Lusimba/mandrill_api.git'
2. Navigate into the repository by running
   - '$ cd mandrill_api'
3. Create a virtual environment to install dependencies by running
   - '$ python3 -m venv env'
4. Activate your virtual environment by running
   - '$ source env/bin/activate'
5. Install dependencies into your virtual environment by running
   - '$ pip install -r requirements.txt'

## Running the application

6. To launcg the application, run
   - '$ uvicorn main:app --reload' in the terminal

## Available paths - view in the browser.

7. Navigate to "http://localhost:8000/" to view live API data
8. Navigate to "http://localhost:8000/dashboard" to view the database records
