print("""Hello and welcome to my general mathematics quiz.
In this quiz you will be asked from 10-50 mathematics questions based on 
your choice.
Also depending on your choice, you can choose to  do either a hard or easy
quiz.
The hard quiz will feature algebra and number, you will also be only 
allowed to answer with word answers. 
With the easy questions you will be asked number questions and the answers
wil be in a multi-choice form. 
I reccomend doing a playthrough of both the quizes at least once. """)
print("I hope you enjoy :)")
while True:
    try:
        name = input("Please enter your name: ")
        if name.isalpha():
          break
    except ValueError:
        print("Not a valid name")
  
print("Hello {} I hope you have fun playing my game".format(name))
while True:
    try:
        age = input("Please enter your age: ")
        age = int(age)
        break
    except ValueError:
        print("Not a valid age! Please try again ...")
  
print("Wow, you are {}".format(age))

qq = { 'What is 2*2 \n a: 4\n b: 5\n c: 3\n' : 'a' , 'What is 3*2\n a: 2\n b: 6\n c: 7 \n' : 'b' , 
             'What is the unit for factorial in maths \n a: ^\n b: %\n c: ! \n' : 'c' }

for key in qq.keys():
    user_answer=input(key).lower().strip()
    if qq.get(key)==user_answer:
        print("Correct!") 
    else:
        print("You're Wrong!")

