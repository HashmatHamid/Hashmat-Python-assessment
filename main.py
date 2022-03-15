print("Hello and welcome to my general mathematics quiz, I hope you enjoy this quiz")
name=input("What is your name? ")
if name == str( ): 
  print("That was not a name")
  name_1=input("What is really your name? ")
  print("Hello {} I hope you have fun playing my game".format(name_1))
else: 
  print("Hello {}, I hope you enjoy my quiz".format(name))
