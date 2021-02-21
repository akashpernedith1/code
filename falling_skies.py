import turtle
import random
import winsound

score=0
lives=3

wn=turtle.Screen()
wn.title("Falling Skies")
wn.bgcolor("green")
wn.bgpic("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/Male-Deer_left.gif")
wn.register_shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/Male-Deer_right.gif")
wn.register_shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/acorn.gif")
wn.register_shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/toySoldier.gif")

#Add the player
player=turtle.Turtle()
player.speed(0)
player.shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/Male-Deer_right.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction="stop"

#Create a list of good guys
good_guys=[]

#Add the good_guys
for _ in range(20):
    good_guy=turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/acorn.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed=random.randint(1, 4)
    good_guys.append(good_guy)

#Create a list of bad guys
bad_guys=[]

#Add the bad_guys
for _ in range(20):
    bad_guy=turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/toySoldier.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed=random.randint(1, 4)
    bad_guys.append(bad_guy)
    
#Make the pen
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font=("Courier", 24, "normal")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)


#Functions
def go_left():
    player.direction="left"
    player.shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/Male-Deer_left.gif")

def go_right():
    player.direction="right"
    player.shape("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/Male-Deer_right.gif")


#Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Main game loop
while True:
    #Update screen
    wn.update()
    
    #Move the player
    if player.direction=="left":
        x=player.xcor()
        x-=3
        player.setx(x)

    if player.direction=="right":
        x=player.xcor()
        x+=3
        player.setx(x)

    #Move the good guys
    for good_guy in good_guys:   
        y=good_guy.ycor()
        y-=good_guy.speed
        good_guy.sety(y)

        #Check if off the screen
        if y<-300:
            x=random.randint(-380, 380)
            y=random.randint(300, 400)
            good_guy.goto(x,y)

        #Check for a collision with the player
        if good_guy.distance(player)<40:
            winsound.PlaySound("Metroid_Door.wav", winsound.SND_ASYNC)
            x=random.randint(-380, 380)
            y=random.randint(300, 400)
            good_guy.goto(x,y)
            score+=10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
            
    #Move the bad guys
    for bad_guy in bad_guys:   
        y=bad_guy.ycor()
        y-=bad_guy.speed
        bad_guy.sety(y)

        #Check if off the screen
        if y<-300:
            x=random.randint(-380, 380)
            y=random.randint(300, 400)
            bad_guy.goto(x,y)

        #Check for a collision with the player
        if bad_guy.distance(player)<40:
            winsound.PlaySound("Siren.wav", winsound.SND_ASYNC)
            x=random.randint(-380, 380)
            y=random.randint(300, 400)
            bad_guy.goto(x,y)
            score-=10
            lives-=1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)
        



wn.mainloop()
