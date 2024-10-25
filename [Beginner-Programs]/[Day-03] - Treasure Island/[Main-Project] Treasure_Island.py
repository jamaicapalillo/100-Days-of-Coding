# DAY 3
# Date: September 22, 2024

# Main Project: Scooby-Doo's Maze of Mysteries

# ========================
print ("""
                                            :\                  
                                            ;\\                 
                                            ; ;;  __            
                                            :/ :-",dP    _.ggp. 
                                            :     (*).-"" :$$$$;
                                            ;              T$$$;
                                           :     _,-        `TP 
                                           ;      `.  _      ;  
                                           ;        "" \    /   
                                           ;            `-+'    
                                           :            .-'     
                                            ;      \;   ;       
                                            :       `--+'-.     
 .---.                                       ;         ;`       
:_    `.                                     :         ;        
  "-,   ;                                   / "-.      :        
     ;  :                                .p""-.  ""--..:        
     ;  :                             .-T$$P   ""--..___l-,     
     ;  :                          .-"   ""            :\()l    
     ;  ;              _________.-"         $$          ;`-'    
     ;  ; bug     .--""$$$$$$$P                         :       
     ;  '._____.-"_.   'T$$P^'                          :       
     :         .-"                                 \    :       
     '.___...-"                                     ;   :       
           /                                        ;   ;       
          :                   .            /       /   /        
          ;                 .J__          :       /  .'         
          ;               .;    "-.       ;      j.-"           
          :             .'/        "-.    ;     : :             
           ;          .' /            "---:     ; ;             
           :       .-"  /                 :    : :              
           ;    .-"  .-"                   ;   ; ;              
          /   .'  .-"                      :  : :               
         /  .'  .'                         :  | ;               
        :  /\  :                           :  ;:                
        ; :  ; ;                           : : ;                
       :  ;  : :__                         ; | :                
       ; _L__J   -`,                      :  : '--.             
       :  l l l____l                       \ _`-,-:             
      ( l ;_:-'                            /___l_|`;             
       """                                            
                                             "        """)


# Greetings
print ("Welcome to the Scooby-Doo's Maze of Mysteries!!")

# Fall into a hole
left_or_right = input ("\nScooby-Doo is facing two pathways ahead of him. Which one should you choose? Left or Right?  ")

# Left = Win. Right or anything else = Game Over.
if left_or_right == "Left":
  print ("\nYou are safe! Keep traveling. Enjoy and Goodluck.")
    # Attacked by trout
  swim_or_not_swim = input ("\nThere is a trout ahead of him. Should he Swim or Not ? ")

  # Wait = Win. Swim or anything else = Game Over.
  if swim_or_not_swim == "Not":
    print ("\nHe's safe. Continue Traveling. Stay safe, you are almost at the finish line.")

    # Which door
    which_door = input ("\nYou are at the last stop. There are 3 colored-door in front of him. Red, Blue, and Yellow. Which one should you choose? ")

    if which_door == "Red": # Red - Burned by fire
      print ("ARGHHH!!! Oh no! He is being burned by fire!!")
    elif which_door == "Blue": # Blue - Eaten by beasts
      print ("OH MY GOSH, He is being eaten by the beasts. Poor Scooby-doo. All of that just for him to became the beast's food.")
    elif which_door == "Yellow": # Yellow - You Win!
      print ("Finally!! All of that hardworks and long journey. Scooby-Doo SURVIVED!! Thank you for your help and support!")
    else: # Anything Else
      print ("That door is not in the options. Therefore, we don't know if Scooby-Doo survived or not.")

  else:
    print ("\nOh no! He got attacked by a trout. Game Over. He's their food now.")

else:
  print ("\nYou mad him fall into a hole. Game Over. He's Dead.")

# Display result
print ("\nGame Over. Better luck next time. See you! \nThank You for playing our Game.")