import turtle, random, time, os

wn = turtle.Screen()
wn.tracer(0)
wn.colormode(255)
wn.bgcolor(200, 200, 200)
wn.setup(800, 600)

rounds = 1
winners = {}
run = True

def create_turtle(color, x, y, id):
  t = turtle.Turtle()
  t.speed(1)
  t.id = id
  t.shape('turtle')
  t.shapesize(3)
  t.color(color)
  t.penup()
  t.goto(x, y)
  return t

def create_list_of_turtles(n_players):
  x_start = 250
  players = []
  id = 1
  for i in range(n_players):
    rgb = [random.randint(0, 255) for i in range(3)]

    t = create_turtle(rgb, -250, x_start, id)
    players.append(t)
    x_start -= 100
    id += 1
  return players

line = turtle.Turtle()
line.speed(0) 
line.pensize(5)
line.penup()
line.goto(350, 300)
line.pendown()
line.goto(350, -300)
line.hideturtle()

n_player = 0

while n_player == 0 or n_player > 6:
  os.system('clear')
  try:
    n_player = int(input('How many players? (Cannot be more than 6 players)\n'))
  except Exception as e:
    print(f'Please, enter a valid number... error {e}' )
    time.sleep(2)

players = create_list_of_turtles(n_player)

#Game logic

dice = list(range(1, 7))

def roll_the_dice():
  chosen_number = random.choice(dice)
  steps = chosen_number * 20
  return steps

def check_if_win(player):
  global players, winners
  if player.xcor() > 300:
    end_time = time.time()
    time_elapsed = end_time - start_time
    winners[player] = time_elapsed
    player.hideturtle()
    players.remove(player)

def move_player(player, steps):
  print(f'The {player.id} turtle will move {steps} steps.')
  player.fd(steps)
  check_if_win(player)

def drawn():
  wn.update()
  

def play():
  global dice, winers, n_player, run
  print(f'\n{rounds}º round:')
  time.sleep(1)
  for player in players:
    steps = roll_the_dice()
    move_player(player, steps)
    drawn()
  if len(winners) == n_player:
    run = False

def processing():
  time.sleep(random.randint(0, 1))

start_time = time.time()

while run:
  drawn()
  wn.ontimer(play(),2000)
  rounds += 1

processing()
os.system('clear')

print('The race ends and here is the outcomes... ')
processing()

print(f'Took {rounds} rounds')
processing()
print('#'*20)
rank = 1
for k, v in winners.items():
  print(f'#{rank} - Turtle:{k.id}\t Time elapsed:{round(v,2)}')
  rank += 1
  processing()