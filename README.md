#2001
##Workshop: Game room (*)

Implement the game 2001, below you will find the rules.

2001 - Game rules
Each player starts with a number of points equal to 0.
In his turn, a player rolls 2 dice (standard hex dice).
The number of eyes thrown is added to the point total.
Starting on the second turn:
if the player throws a 7, he divides his number of points by that value discarding the fractional part,
if he throws 11, he multiplies his current number of points by that value.
The player who first reaches 2001 points wins.
Implementation
Implement the game in a two-player version.
Let it be a console application.
Let the second player be a computer.
Display the current number of points after each round.
The player's throw should take place after the user presses the enter key. 
The computer's throw occurs automatically, after the player's throw. 
End the program when either the player or the computer reaches more than 2001 points.
Modification 1
You may have noticed that the current version of the game is not very interactive and that it is all about clicking the enter key.
 Let's try to make it a little more interactive.

Before each throw, give the player a choice.
Let him choose 2 dice from the set: D3, D4, D6, D8, D10, D12, D20, D100.
The dice can be repeated, or the player can use 2 different dice.
Have the player select the dice by entering the appropriate string (one for each dice).
You can use the code from the Dice task.
Let the computer's choice of dice be random.
The rest of the rules remain the same.

Modification 2
Now try to transfer your game to the server using Flask. 
To store information between turns, use hidden form fields. 
This is not the best solution (it can be prone to cheating), but we don't care about that for now. 
Dice selection before the throw, should be done using the form.

Translated with www.DeepL.com/Translator (free version)