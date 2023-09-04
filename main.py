# part1
def padel_court_cost(court_type):
    if court_type=="indoor":
        return 30
    else:
        return 20

 # part2
def rackets_cost(racket_brand):
    if racket_brand=="Bullpadel":
      return 100
    elif racket_brand=="Nox":
      return 140
    elif racket_brand=="Siux":
      return 200
          
# part3
def padel_balls_cost(ball_boxes):
    if ball_boxes==1:
      return 2
    elif ball_boxes==2:
      return 3.5
    elif ball_boxes==3:
      return 5
    
# part4
def padel_game_cost():
   court = (input("enter the court type:"))
   rackets = (input("enter racket brand:"))
   balls = int(input("enter number of ball boxes:"))
   result = padel_court_cost(court) + rackets_cost(rackets) + padel_balls_cost(balls)
   return result

print(padel_game_cost())


    