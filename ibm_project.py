# Quiz Application Project
print("===================================================")
print("                  Quiz Application                 ")
print("====================================================")

print("Welcome to the Quiz!")
print("Test your knowledge")
print("Let's get started")

name = input("Enter your name: ")
print("Welcome, " + name)
print("Let's begin the quiz!")

score = 0

print("\n Question 1:")
print("Which function is used to display output in python?")
print("A. input() \nB. print() \nC. type() \nD. int()")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\n Question 2:")
print("Which symbol is used for comments in Python?")
print("A. // \nB. !-- \nC. # \nD. **")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "C":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\n Question 3:")
print("Which data type stores True or False?")
print("A. String \nB. Integer \nC. Float \nD. Boolean")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "D":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\n Question 4:")
print("Which function accepts input from the user?")
print("A. print() \nB. input() \nC. range() \nD. len()")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\nQuestion5:")
print("Which symbol is used for multiplication in Python?")
print("A. X \nB. / \nC. * \nD. %")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "C":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\nQuestion6:")
print("Which symbol is used to assign a value to a variable?")
print("A. == \nB. = \nC. != \nD. > ")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\nQuestion7:")
print("Which data type is used for whole numbers?")
print("A. str \nB. int \nC. float \nD. bool")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\nQuestion8:")
print("Which keyword is used to check a condition?")
print("A. if \nB. print \nC. input \nD. int")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "A":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
print(f"Your current score is : {score}")

print("\nQuestion9:")
print("Which loop is commonly used to repeat code a fixed number of times?")
print("A. if \nB. for \nC. else \nD.print")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer!")
print(f"Your current score is : {score}")

print("\nQuestion10:")
print("What is the output of print(2 ** 3)?")
print("A. 6 \nB. 8 \nC. 9 \nD. 10")
answer = input("Enter your answer (A/B/C/D): ").upper()
while answer not in ["A", "B", "C", "D"]:
    print("Invalid option!Please select A, B, C, D.")
    answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer!")
print(f"Your current score is : {score}")

print("\nQuiz completed!")
print(f"Your final score is {score} /10")
percentage = (score/10) * 100
print(f"Your percentage is: {percentage} %")

if percentage >= 80:
    print("Excellent work!")
elif percentage >= 50:
    print("Good job! Keep practising.")
else:
    print("Keep learning and try again")
