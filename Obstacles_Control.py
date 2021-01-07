#Timer and Score objects
from graphics import *
def Obstacle_Control(Screen,Ball,Wall):
    Clock_Divider=0
    Timer=0
    Score=0
    GO=0
    while GO == 0:
     Clock_Divider=Clock_Divider+1
     Score=Score+1
     TrS=1000000
     "Start with Graphic Control and values"
     if Time == 10000000:
         Timer= 1+Timer
         Clock_Divider=0
     else:
         Timer=Timer

     if Score ==  100:
         TrS=TrS-50 #Screen refresh rate of the game for faster and challenging gamee
     elif Score == 300:
         TrS=TrS-100
     elif Score == 500:
         TrS=TrS-300
     else:
         TrS=TrS
     if "Yaxis of the Circle Center "== 0:
         GO==1
     else:
         GO==0
    return Final_Time, Final_Score
