import turtle
import math
import random

wn=turtle.Screen()
wn.setup(width=800, height=800)
wn.title("Space Station Defense Game")
wn.bgpic("C:/Users/Aaron/Onedrive - Hillsborough County Public Schools/.py_(Python)/space.gif")
wn.bgcolor("black")
#Stops screen updates
wn.tracer(0)

#Register shapes
player_vertices=((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18,5),(15,0))
wn.register_shape("player",player_vertices)

asteroid_vertices=((0,10),(5,7),(3,3),(10,0),(7,4),(8,-6),(0,-10),(-5,-5),(-7,-7),(-10,0),(-5,4),(-1,8))
wn.register_shape("asteroid", asteroid_vertices)

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #Maximum animation speed
        self.speed(0)
        self.penup()

def get_heading_to(t1, t2):
    x1=t1.xcor()
    y1=t1.ycor()
    x2=t2.xcor()
    y2=t2.ycor()

    heading=math.atan2(y1-y2, x1-x2)
    heading=heading*180.0/3.14159
    return heading

player=Sprite()
player.color("white")
player.shape("player")
player.score=0

missiles=[]
for _ in range(3):
    missile=Sprite()
    missile.color("red")
    missile.shape("arrow")
    missile.speed=0.4
    missile.state="ready"
    missile.hideturtle()
    missiles.append(missile)

pen=Sprite()
pen.color("white")
pen.hideturtle()
pen.goto(0, 350)
pen.write("Score: 0", False, align="center", font=("Arial", 24, "normal"))


asteroids=[]
for _ in range(5):
    asteroid=Sprite()
    asteroid.color("brown")
    asteroid.shape("asteroid")
    asteroid.speed=random.randint(0, 100)/1000
    asteroid.goto(0, 0)
    heading=random.randint(0, 360)
    distance=random.randint(400, 600)
    asteroid.setheading(heading)
    asteroid.fd(distance)
    asteroid.goto(400, 0)
    asteroid.setheading(get_heading_to(player, asteroid))
    asteroids.append(asteroid)

def rotate_left():
    player.lt(10)

def rotate_right():
    player.rt(10)

def fire_missile():
    for missile in missiles:
        if missile.state=="ready":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state="fire"
            break

#Keyboard binding
wn.listen()
wn.onkey(rotate_left, "Left")
wn.onkey(rotate_right, "Right")
wn.onkey(fire_missile, "space")

#Start main game loop
while True:
    #Do screen updates
    wn.update()
    player.goto(0, 0)    

    #Move the missile
    for missile in missiles:
        if missile.state=="fire":
            missile.fd(missile.speed)

        #Border checking
        if missile.xcor()>400 or missile.xcor()<-400 or missile.ycor()>400 or missile.ycor()<-400:
            missile.hideturtle()
            missile.state="ready"

    #Iterate through asteroids
    for asteroid in asteroids:
        #Move the asteroid
        asteroid.fd(asteroid.speed)

        #Check for collisions
        #Asteroid and Missile
        for missile in missiles:
            if asteroid.distance(missile)<20:
                #Reset Asteroid
                heading=random.randint(0, 360)
                distance=random.randint(800, 1000)
                asteroid.setheading(heading)
                asteroid.fd(distance)
                asteroid.setheading(get_heading_to(player, asteroid))
                asteroid.speed+=0.01

                #Reset Missile
                missile.goto(1000, 1000)
                missile.hideturtle()
                missile.state="ready"

                #Increase score
                player.score+=10
                pen.clear()
                pen.write("Score: {}".format(player.score), False, align="center", font=("Arial", 24, "normal"))
                
        #Asteroid and Player
        if asteroid.distance(player)<20:
            #Reset Asteroid
            heading=random.randint(0, 360)
            distance=random.randint(800, 1000)
            asteroid.setheading(heading)
            asteroid.fd(distance)
            asteroid.setheading(get_heading_to(player, asteroid))
            asteroid.speed+=0.01
            print("Player killed!")
            player.score-=50
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align="center", font=("Arial", 24, "normal"))


