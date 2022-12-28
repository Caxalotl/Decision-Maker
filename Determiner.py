from turtle import Screen, Turtle, mainloop
import random
EightBall = ['Yes', 'No', 'Maybe']
writer = Turtle()
writer.ht()
writer.pu()
writer.goto(1,1.15)
writer.write( random.choice(EightBall),align="center",font=("ModeSeven",30,("bold")))
mainloop()
