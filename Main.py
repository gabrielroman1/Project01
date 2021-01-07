#Reach to the top
from Game_Objects import *
from graphics import *
from Obstacles_Control import *
def main():
    Power="On"
    Screen,Ball,Wall=Game_Object()
    
    while Power == "On":
      
      FT,FSC=Obstacle_Control(Screen,Ball,Wall)
      
      Print("Final Time: ",FT,"\nFinal Score: ",FSC,"\n\n")
      PowerD=input("Do you want to exit game: ")
      
      if PowerD == "Yes" or PowerD=="y" or PowerD == "Y":
        print("Good bye")
        Screen.close()
        Power == "Off"

      else:
        Power=="On" 

main()
