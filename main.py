from game_data import data
# print(len(data))

import art
logo = art.logo
vs = art.vs


import random

# choose 2 to start with from data


# print all data with vs sign


# take input from player


# make a function compare if he wins or not
# iff win store score
# next time show score
# now ask to compare 2nd and 3rd random data
# if loose then set game over

def compare(a, b):
  if data[a]["follower_count"] > data[b]["follower_count"]:
    return True
  else:
    return False

def data_print(a, b):
  
  print(f"Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}")
  print(vs)
  print(f"Compare B: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}")

print(logo)

a = 0
b = 0

while a == b:
  a = random.randint(0,49)

  b = random.randint(0,49)

score = 0
game_over = False
while not game_over:

    data_print(a,b)
    answer = input("Who has more followers? Choose 'A' or 'B' : ")

    if answer == 'a':
        if compare(a, b) == True:
            score += 1
            print(f"You'r right! Your current score {score}.")
        else:
            print(f"You'r wrong! Your current score is {score}.")
            game_over = True
    elif answer == 'b':
        if compare(b, a) == True:
            print("you won")
            score += 1
        else:
            print("you loose")
            game_over = True
    else:
        print("You choose wrong opption\nGame over!")
    a = b
    b = random.randint(0,49)