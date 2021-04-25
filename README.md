# Zadanie nr 3. Software Engineer 
Solution of task is a server side, which provides services 

Running this application on a local environment
## Tech/framework used:

[Python 3.8](https://www.python.org/downloads/release/python-380/)

[Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Installation

* You need to clone the repository
* Create a python virtual environment
* Activate it and install with `pip` required packages from `requirements.txt`. 

1. Downloading sources
    ```bash
    git clone https://github.com/prowincial/task-for-allegro.git
    cd task-for-allegro
    ```
2. Installing virtual environment
    ```bash
    # Linux terminal
    python3 -m venv venv
    . venv/bin/activate
    ```
    
    ```cmd
    :: Windows cmd
    py -3 -m venv venv
    venv\Scripts\activate.bat
    ```
3. Installing required dependencies
    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

### Usage

1. Set environment variable
    ```bash
    $ export FLASK_APP=mserver
    ```
2. Running the app
    ```bash
    $ flask run
    ```
This starts the application and can be viewed from the following URL: http://localhost:5000 in your laptop.

3. Listing of repositories (name and number of stars),
open new command prompt
make curl request in command prompt
```bash
$ curl http://127.0.0.1:5000/api/v0.1/<string:username>/repos
```
4. Returning the sum of stars in all repositories
open new command prompt
make curl request in command prompt
```bash
$ curl http://127.0.0.1:5000/api/v0.1/<string:username>/stargazers
```

## Tests
To run tests:
open new command prompt
install virtual environment and required dependencies
run tests
```bash
pytest tests/conftest.py
```

## Future development

The best solution for further development of the application would be to put it in a docker container,
so the flexibility, speed and scalability of the project will increase

