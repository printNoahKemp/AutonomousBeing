"""Seek behaviour in py Turtle"""

import turtle, numpy as np, math

WIDTH,HEIGHT = 700,400

###
pos=np.array([0,0])
vel=np.array([0,0])
acc=np.array([0,0])
###

def Update(vel,pos,acc):
    vel = np.add(vel, acc)
    pos = np.subtract(pos, vel)
    acc = np.multiply(acc,[0,0])
    return pos, vel, acc

def Apply(force,acc):
    acc = np.add(acc,force)
    return acc

def Seek(target,pos,max_speed,vel,acc):
    desired_vel = pos - target
    desired_vel = desired_vel/math.sqrt(desired_vel[0]*desired_vel[0]+desired_vel[1]*desired_vel[1])
    desired_vel = desired_vel * max_speed
    
    steering_vel = desired_vel - vel
    return Apply(steering_vel,acc)

agent = turtle.Turtle()
agent.penup()

while True:
    agent.goto(pos)
    acc = Seek((200,200),pos,0.2,vel,acc)
    pos,vel,acc=Update(vel,pos,acc)