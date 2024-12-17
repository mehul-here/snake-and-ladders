def snake(x):
  head_of_snake=[12,36,89,98,77]
  tail_of_snake=[1,10,42,9,24]
  return tail_of_snake[head_of_snake.index(x)]
def ladder(x):
  tail_of_ladder=[88,7,47,87,3]
  head_of_ladder=[91,99,92,90,71]
  return head_of_ladder[tail_of_ladder.index(x)]
def win(name):
  print(f"{name} won the game")
  print(f"Now {name} will give everyone in the game chapoo!!!!!")
  print("Hehehe")
  return True
def dice(position,name):
  import random as rd
  while(True):
    roll=rd.randint(1,6)
    if(position>=0):
      position=position+roll
      if(position>=99):
        print(f"{name} reaches 99 as {name} rolls {roll}")
        win(name)
        position=99
        break
      if(roll==6):
        print(f"{name} rolled a 6 and gets another turn , so now {name} is at {position}")
      else:
        print(f"{name} rolled a {roll} , now {name} is at {position}")
      if(position in [88,7,47,87,3]):
        position1=ladder(position)
        print(f"{name} climbed the ladder at {position} and is now at {position1}")
        position=position1
        if(position==99):
          win(name)
          break 
      elif(position in [12,36,89,98,77]):
        position1=snake(position)
        print(f"{name} got bitten by the snake  at {position} and is now at {position1}")
        position=position1
    if(position<0):
      if(roll==6):
        print(f"{name} rolls a 6 and unlocks his piece")
        position=0
      else:
        print(f"{name} rolls a {roll} so his piece is not unlocked ")
    if(roll!=6):
      break
  return position 
def main():
  n=input("Enter number of player: ")
  while not n.isdigit():
    print("Enter a valid input")
    n=input("Enter number of player: ")
  n=int(n)
  names=[]
  for i in range(n):
    name=input(f"Enter name of player {i+1}: ")
    names.append(name)
  positions=[]
  for i in range(n):
    positions.append(-1)
  while(True):
    for i in range(n):
      positions[i]=dice(positions[i],names[i])
      if(positions[i]==99):
        break
    if(99 in positions):
      break
if(__name__=="__main__"):
  main()
