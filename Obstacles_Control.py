#Timer and Score objects
from graphics import *
def Obstacle_Control(Screen,Ball,Wall): 
    
    Clock_Divider=0
    Tap=0
    Timer=0
    TrS=10000000
    Score=0
    GO=0
    W3=0
    W2=0
    Wall[0].draw(Screen)     
    while GO == 0:
      Clock_Divider=Clock_Divider+1
      if Clock_Divider == 100000:
        Timer= 1+Timer
        Clock_Divider=0
      else:
        Timer=Timer 
 
      if TrS <= 0:
        TrS=1000000
        if (Wall[0].getP2()).getY()< 0:
          Wall[0].move(0, 500-(Wall[0].getP2()).getY())
          Score=Score+100
          Tap=Tap+1
        else:
          Wall[0].move(0,-3)
          Score=Score
      else: 
         if Score >=  100 and Score < 300:
            TrS=TrS-50 #Screen refresh rate of the game for faster and challenging game
         elif Score >=  300 and Score < 500:
            TrS=TrS-100
         elif Score >= 500:
            TrS=TrS-300
         else:
            TrS=TrS-1
         
      if(Ball.getCenter()).getY()== 0 or Tap == 5:
         GO=1
      else:
         GO=0
            
    Final_Time=Timer
    Final_Score=Score

     
    return Final_Time,Final_Score

