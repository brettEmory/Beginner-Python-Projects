#This is a simple python program that was used to practice user input as well as help me study for my exams!
print("Hello Welcome to my Computer Quiz Game")

play = input("Would you like to play my game? (yes or no) \n")

#check user input to either play or quit
if play != "yes":
    print("Too bad... \nBye")
    quit()

print("Awesome! lets play! \n")

#user score
score = 0
#First question, and if else to handle user answer
answer = input("What does CPU stand for?\n")
if answer.lower() != ("central processing unit"):
    print("Sorry, the correct answer was: \'central processing unit\'")
    print("your score is: " + str(score))
else:
    score = score+1
    print("Correct! Your score is: " + str(score) + "\n\n")

answer = input("What does GPU stand for\n")
if answer.lower() != ("graphics processing unit"):
    print("Sorry, the correct answer was: \'graphics processing unit\'")
    print("your score is: " + str(score))
else:
    score = score+1
    print("Correct! Your score is: " + str(score) + "\n\n")


answer = input("What does PSU stand for?\n")
if answer.lower() != ("power supply unit"):
    print("Sorry, the correct answer was: \'power supply unit\'")
    print("your score is: " + str(score))
else:
    score = score+1
    print("Correct! Your score is: " + str(score) + "\n\n")


print("Thank you for playing my game I hope you got the answers correct!")
quit()


