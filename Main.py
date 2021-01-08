#Reach to the top
from Game_Objects import *
from graphics import *
from Obstacles_Control import *
def main():
    Power="On"
    Screen,Ball,Wall=Game_Object()
    
    while Power == "On":
      #GUI for playing Answer (If we have the time) if not, it will go with the 
      #terminal menu
      FT,FSC=Obstacle_Control(Screen,Ball,Wall)
      
      print("Final Time: ",FT,"\nFinal Score: ",FSC,"\n\n")
      #File Write the final Score and Time algorithm
      PowerD=input("Do you want to exit game: ")
      
      if PowerD == "Yes" or PowerD=="y" or PowerD == "Y":
        print("Good bye")
        Screen.close()
        Power == "Off"

      else:
        Power=="On" 

main()
