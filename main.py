print("""Hello and welcome to my general mathematics quiz.
In this quiz you will be asked from 10-50 mathematics questions based on your choice.
Also depending on your choice, you can choose to  do either a hard or easy quiz.
The hard quiz will feature algebra and number, you will also  be only allowed to answer with word answers. 
With the easy questions you will be asked number questions and the answers wil be in a multi-choice form. 
I reccomend doing a playthrough of both the quizes at least once. """)
print("I hope you enjoy :)")
name=input("What is your name? ")
if name == str( ): 
  print("That was not a name")
  name_1=input("What is really your name? ")
  print("Hello {} I hope you have fun playing my game".format(name_1))
 
else: 
  print("Hello {}, I hope you enjoy my quiz".format(name))
x = "1"

if not type(name) is str:
  raise TypeError("Only strings are allowed")
else: print("Hello {}, I hope you enjoy my quiz".format(name))
