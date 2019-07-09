import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': 'Get your neck chopped!',
        'head_url': head_url,
        'name': 'NinjaGaiden Snake'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    return {
        'move': findFood(data),
        'taunt': 'Come get some!'
    }

def getSnake(gameState, id):
   for snake in gameState["snakes"]:
       if snake["id"] == id :
        return snake
def findFood(gameState):

  mySnake = getSnake(gameState, gameState["you"])
  head = mySnake["coords"][0]
  if gameState["food"][0][0] < head[0]: 
        move = "left"


  if gameState["food"][0][0] > head[0]:
        move = "right"


  if gameState["food"][0][1] < head[1]:
        move = "up"


  if gameState["food"][0][1] > head[1]:
        move = "down"
  return move 

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
