# Mason Mah, Jaime Villa, Aracely Cano-Gramajo




import turtle              # 1.  import the modules
import random
import time
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightgreen')
lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
ricky = turtle.Turtle()
ricky.ht()
lance.ht()                 # We don't want to show the turtles setting up
andy.ht()
                            #This turtle is only used to show the finish line
finishline =turtle.Turtle()
finishline.ht()
finishline.pu()
finishline.clear()
finishline.speed(100)
finishline.pensize(5)
finishline.goto(190,-100)
finishline.pd()
finishline.goto(190,100)
finishline.pu()


writetext=turtle.Turtle()    # This turtle will print the text onscreen
writetext.ht()               # writetext should be completely hidden
writetext.pu()
writetext.clear()            # First we print a little introduction
writetext.goto(0,150)        # The intro is at the top
writetext.write("""
Welcome To The First Annual
CMPS 5P Turtle Race""", align = 'center',font=("Verdana",10,"bold"))
time.sleep(2)
writetext.clear()
writetext.write("""
The Champion, Turtle Andy, will be wearing Blue""", align = 'center',font=("Verdana",10,"bold"))
time.sleep(2)
writetext.clear()
writetext.write("""
His Rival, Turtle Lance, will be wearing Red""", align = 'center',font=("Verdana",10,"bold"))
time.sleep(2)
writetext.clear()
writetext.write("""
The Newcomer, Turtle Ricky, will be wearing Green""", align = 'center',font=("Verdana",10,"bold"))
time.sleep(1)
writetext.goto(0,-150)      # This moves the text to the bottom of screen
lance.shape('turtle')
andy.shape('turtle')
ricky.shape('turtle')
lance.color('red')          # Lance = Red, Andy = Blue
andy.color('blue')
ricky.color('green')
andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
ricky.up()
restartvariable = "Y"         # The variable for restarting the race
while restartvariable.lower() == 'y':  # Y and y are acceptable answers
  andy.clear()
  lance.clear()
  ricky.clear()
  ricky.color('green')
  lance.color('red')
  andy.color('blue')       # At the end of the race, the winner is gold
  andy.goto(-180, 40)
  ricky.goto(-180,-40)
  lance.goto(-180,0)      # We have to put them back to red/blue
  andy.st()
  ricky.st()
  lance.st()                #Once they are in starting positions we show them

  def turtlesMove(andy, lance, ricky):  #This function moves them a little at a time
    andy.forward(random.randrange(2,7)) # 2-7 seems to be a good balance
    ricky.forward(random.randrange(2,7))
    lance.forward(random.randrange(2,7)) #Not too slow and not too fast

  def turtlesRace(andy,lance, ricky):   #This function handles the race part
    while andy.xcor() < 170 and lance.xcor() < 170 and ricky.xcor() < 170: #180 is the finish line
      turtlesMove(andy,lance,ricky)    # This calls the function above
    time.sleep(0.2)                #Wait a moment  before changing their color
    if (andy.xcor() > lance.xcor() and andy.xcor() > ricky.xcor()):
      andy.fillcolor("gold")      #First place gets gold paint
      writetext.write("Turtle Andy Won The Race", align = "center", font=("Verdana", 15, "bold"))
    elif (andy.xcor() < lance.xcor() and lance.xcor() > ricky.xcor()):
      writetext.write("Turtle Lance Won The Race", align = "center", font=("Verdana", 15, "bold"))
      lance.fillcolor("gold")
    elif (ricky.xcor() > andy.xcor() and ricky.xcor() > lance.xcor()):
      writetext.write("Turtle Ricky Won the Race", align="center", font= ("Verdana", 15, "bold"))
      ricky.fillcolor("gold")
    else:                      # Occaisonally two will hit 180 at the same time
      writetext.write("The Race Was A Tie", align = "center", font=("Verdana", 15, "bold"))

  # This is the start of each race
  writetext.clear()
  writetext.write("Ready...", align = "center", font=("Verdana", 10, "bold"))
  time.sleep(1)
  writetext.clear()
  writetext.write("Set... ", align = "center", font=("Verdana", 30, "bold"))
  time.sleep(1)
  writetext.clear()
  writetext.write("GO!!!!!", align = "center", font=("Verdana", 50, "bold"))
  time.sleep(1)
  writetext.clear()
  turtlesRace(andy,lance,ricky)     # Call the race function to do the work
  time.sleep(2)               # Wait 2 seconds before asking for another race
  writetext.clear()
  restartvariable = input("Press Y to Race Again") #Ask user if they want to race again
writetext.write("The End",align = "center", font=("Verdana",50,"bold")) # the end!
wn.exitonclick()
