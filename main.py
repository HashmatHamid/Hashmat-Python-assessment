#this is the introduction  to my quiz
def intro():
    print("""Hello and welcome to my general mathematics quiz.
In this quiz you will be asked from 10-50 mathematics questions based on 
your choice.
Also depending on your choice, you can choose to  do either a hard or easy
quiz.
The hard quiz will feature algebra and number, you will also be only 
allowed to answer with word answers. 
With the easy questions you will be asked number questions and the answers
wil be in a multi-choice form. """)
    print("I hope you enjoy :)")


#this is where user gets asked to input their name
def name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():
              break
        except ValueError:
            print("Not a valid name")
     
    print("Hello {} I hope you have fun playing my game".format(name))  
#this is where user gets asked to input their age

def age():
    while True:
        try:
            age = input("Please enter your age: ")
            age = int(age)
            break
        except ValueError:
            print("Not a valid age! Please try again ...")
     
    print("Wow, you are {}".format(age))  
   
#all my questions
def questions():
    global score
    score=0
    qq = { 'Q.1) What is 2*2 \n a: 4\n b: 5\n c: 3\n' : '4' , 'Q.2) What is 3*2\n a: 2\n b: 6\n c: 7 \n' : '6' ,
                 'Q.3) What is the unit for factorial in maths \n a: ^\n b: %\n c: ! \n' : '!' , 'Q.4) What is the equation for a question using the pythagoras theorem \n a: a^2+b^2=c^2\n b: b^2+c^2=a^2\n c: c^2+a^2=b^2 \n' : 'a^2+b^2=c^2' , 'Q.5) What is the value of pi \n a: 2.5\n b: 3.14\n c: 0.1 \n' : '3.14' , 'Q.6) What is 2 squared \n a: 4\n b: 2\n c: 1\n' : '4' , 'Q.7) What is the square root of 81 \n a: 9\n b: 13\n c: 10 \n' : '9' , 'Q.8) What is the value of Gst \n a: 15%\n b: 1.5%\n c: 0.15% \n' : '15%' , 'Q.9) Where did the person who invented Algorthm die \n a: Baghdad\n b: London\n c: Beijing\n' : 'Baghdad' , 'Q.10) What year did Stephen Hawking die \n a: 2018\n b: 2019\n c: 2017 \n' : '2018' 
         }
   
    for key in qq.keys():
        user_answer=input(key).lower().strip()
        if qq.get(key)==user_answer:
            print("Correct!")
            score+=1
        else:
            print("You're Wrong!")

   
   
#printing functions
intro()    
name()
age()
questions()
#print score
print("You got "+str(score)+" right!")