# battlesnake-nodejs

A simple [BattleSnake AI](http://battlesnake.io) written in Python. 

To get started you'll need a working Python development environment, and at least read the Heroku docs on [deploying a Python app](https://devcenter.heroku.com/articles/getting-started-with-python). This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on Heroku. Dependencies are listed in [requirements.txt](requirements.txt).

## Pre-requisite Accounts
Every team must show up with a laptop and create the following accounts in order to use the provided start snake. You are welcome to use existing accounts if you have them already.
* Create a free account on Github - https://www.github.com/
* Create a free account on Heroku - https://www.heroku.com/

## Prerequisite Software
You'll need the follwing software on your computer before you can get started with this project:
- [GitHub CLI 2.x](https://git-scm.com/downloads)
- [Heroku CLI 5.x](https://cli.heroku.com/).

You'll need the following software on your computer if you want to compile and run the application locally. This is completely optional but probably desired since troubleshooting coding errors and testing behaviour will be much easier. 
- [Python 2.7](http://hackercodex.com/guide/python-development-environment-on-mac-osx/)
- [pip 8.x](https://pip.pypa.io/en/latest/installing.html)

If you have the software installed already, confirm by running the respective commands on the command prompt and check the versions:
- ```python --version```
- ```pip --version```
- ```git --version```
- ```heroku --version```

## Preparing your project
**DON'T SKIP THIS STEP**. You'll need your own copy of this project under your own GitHub account in order to make and publish changes to your snake.
- Make sure you are signed in to your GitHub account
- Fork this [project](https://github.com/xmatters-tko/xm-battlesnake-java/fork)

## Test Your Environment Setup
At this point, make sure that all of you software is installed, and you've forked this project correctly. Run the following commands:

```sh
$ git clone https://github.com/<your account>/xm-battlesnake-python.git
$ cd xm-battlesnake-python
$ pip install -r requirements.txt
$ python app/main.py
```

Your app should now be running on [localhost:5000/health](http://localhost:5000/health).

### Testing your local app
You can use curl commands to easily test if you snake is working and responding to end points.

Run it locally using heroku command:
```
$ heroku local
```
#### /start Endpoint
```
$ curl localhost:5000/start -X POST -H "Content-Type: application/json" -d '{"width":20,"height":20,"game_id":"example-game-id"}'
```
#### /move Endpoint
```
$ curl localhost:5000/move -X POST -H "Content-Type: application/json" -d '{ "you": "2c4d4d70-8cca-48e0-ac9d-03ecafca0c98","width": 2,"turn": 0,"snakes": [{ "taunt": "git gud","name": "my-snake","id": "2c4d4d70-8cca-48e0-ac9d-03ecafca0c98","health_points": 93,"coords": [[0,0],[0,0],[0,0]] },{ "taunt": "gotta go fast","name": "other-snake","id": "c35dcf26-7f48-492c-b7b5-94ae78fbc713","health_points": 50,"coords": [[1,0],[1,0],[1,0]] }],"height": 2,"game_id": "a2facef2-b031-44ba-a36c-0859c389ef96","food": [[1,1]],"dead_snakes": [{ "taunt": "gotta go fast","name": "other-snake","id": "83fdf2b9-c8d0-44f4-acb2-0c506139079e","health_points": 50,"coords": [[5,0],[5,0],[5,0]] }] }'
```

## Deploying to Heroku

You will be provided a heroku project name to deploy your snake to
inside your git repo  do the following commands 
```sh
$ heroku git:remote -a [HEROKU_PROJECT_NAME]
```
then everytime you want to deploy changes you can simply do  
```sh
 $ git push heroku master
```
The output should end with the URL endpoint of your snake. Use this URL to add your snake to a game on the server.
```
remote: -----> Launching...
remote:        Released v3
remote:        https://my-snake.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
```
#### Testing the app
Your app should now be running on [https://my-snake.herokuapp.com/health](https://my-snake.herokuapp.com/health). You can use curl commands to easily test if you snake is working and responding to end points.

#### /start Endpoint
```
$ curl https://my-snake.herokuapp.com/start -X POST -H "Content-Type: application/json" -d '{"width":20,"height":20,"game_id":"example-game-id"}'
```
#### /move Endpoint
```
$ curl https://my-snake.herokuapp.com/move -X POST -H "Content-Type: application/json" -d '{ "you": "2c4d4d70-8cca-48e0-ac9d-03ecafca0c98","width": 2,"turn": 0,"snakes": [{ "taunt": "git gud","name": "my-snake","id": "2c4d4d70-8cca-48e0-ac9d-03ecafca0c98","health_points": 93,"coords": [[0,0],[0,0],[0,0]] },{ "taunt": "gotta go fast","name": "other-snake","id": "c35dcf26-7f48-492c-b7b5-94ae78fbc713","health_points": 50,"coords": [[1,0],[1,0],[1,0]] }],"height": 2,"game_id": "a2facef2-b031-44ba-a36c-0859c389ef96","food": [[1,1]],"dead_snakes": [{ "taunt": "gotta go fast","name": "other-snake","id": "83fdf2b9-c8d0-44f4-acb2-0c506139079e","health_points": 50,"coords": [[5,0],[5,0],[5,0]] }] }'
```

### Pushing Updates to Heroku
You have to commit your changes to your git project as part of pushing them to the remote heroku git.
```sh
$ git add --all; git commit -m "Updated"; git push
$ git push heroku master
```

### Debugging Logs on Heroku
Once your snake is running, you can tail the logs any time in the console using the command:
```sh
$ heroku logs --tail
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
