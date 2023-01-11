print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("You are at a cross road. Where do you want to go?\n") 
direction = input("Type 'left' or 'right'\n")
direction = direction.lower()

if direction == "right":
    print("\nYou fell into a hole. Game Over.")
    print('''
     SSSSSS
.ss.  SP""YS
SSSS  S    S
`SS'  S.  .S
      SSSSSS

    ''')
else:
    print("\nYou came to a lake. There is an island in the middle of the lake.\n")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    action = input()
    action = action.lower()

    if action == "swim":
        print("\nYou were attacked by an angry trout. Game Over.")
        print('''
            /"*._         _
      .-*'`    `*-.._.-'/
    < * ))     ,       ( 
      `*-._`._(__.--*"`.\
            ''')
    else:
        print("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        door = input("\nType 'red', 'yellow' or 'blue'\n")
        door = door.lower()

        if door == "red":
            print("\nIt's a room full of fire. Game Over.")
            print('''
                ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
            ''')
        elif door == "yellow":
            print("\nYou found the treasure! You Win!")
            print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`

            ''')

        elif door == "blue":
            print("\nYou enter a room of beasts. Game Over.")
            print('''
                           (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            ''')
        else:
            print("\nYou chose a door that doesn't exist. Game Over.")