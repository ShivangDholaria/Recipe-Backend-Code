# Recipe Management App Backend

## Getting started

### Setting up a project

* Install [`python`](https://www.python.org/downloads/) in your system if you dont have it installed.

* Move into your projects directory: `cd ~/YOUR_PROJECTS_DIRECTORY`

* Clone this repository: `git clone https://github.com/ShivangDholaria/Recipe-Backend-Code.git YOUR_PROJECT_NAME`

* Move into the project directory: `cd YOUR_PROJECT_NAME`

* Create virtual environment for the project using `venv`,
```python
python -m venv .venv
``` 
* Activate the environment using the following command:
```python
.venv\Scripts\python
```

* Install the dependencies: `pip install -r requirements.txt`

### Working on the project

* Move into the project directory: `cd ~/YOUR_PROJECTS_DIRECTORY/YOUR_PROJECT_NAME`
* Run the development task: `python ./manage.py runserver <PORT NUMBER>`
    * Starts a server running at http://localhost:\<PORT NUMBER\>, if port number is not mentioned, the default is 8000.
    * Server will not reflect any live changes made so you will need to stop and start the server again after saving the changes made

## Databases

By default, the project uses SQLite as its default database. If you want to use your own database such as MySQL, Postgres, etc, you can do it by updating the `DATABASES` section in `settings.py` file present in [backend](./backend/) directory of this project.

