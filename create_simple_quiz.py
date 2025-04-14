"""
Create a program that ask user for a question, 
it will also ask for 4 possible answer (a,b,c,d)
and the correct answer. Write the collected data
to a text file. Ask another question until the
user chose to exit.

"""
import time
import os

base_name = input("File name of quiz: ")
time_stamp = time.strftime("%d%m%Y_%H%M%S")
file_name = f"{base_name}_{time_stamp}.txt"

def add_question():
    global file_name
     #ask for inputs (question, possible answers, and correct answer)
    question = input("Enter a question: ").strip()
    option_a = input("Enter option a: ").strip()
    option_b = input("Enter option b: ").strip()
    option_c = input("Enter option c: ").strip()
    option_d = input("Enter option d: ").strip()
    correct_answer = input("Enter Correct answer: ").strip()

    #write the collected data to a .txt file
    with open(file_name,"a") as quiz_file:
        quiz_file.write("Question: " + question + "\n")
        quiz_file.write("A. " + option_a + "\n")
        quiz_file.write("B. " + option_b + "\n")
        quiz_file.write("C. " + option_c + "\n")
        quiz_file.write("D. " + option_d + "\n")
        quiz_file.write("Correct Answer: " + correct_answer + "\n")

def view_questions():
    global file_name
    #read the file 
    if not os.path.exists(file_name):
        print("no question saved yet.\n")
        return
        
    print("contents of current file: \n")
    with open(file_name, "r") as quiz_file:
        print(quiz_file.read())

while True:
    print("\n QUIZ BUILDER MENU")
    print("1. Add a new question")
    print("2. View saved questions")
    print("3. Exit\n")

    choice = input("Select option (1/2/3): ").strip()

    if choice == '1':
        add_question()
    elif choice == '2':
        view_questions()
    elif choice == '3':
        print("Goodbye")
        break
    else:
        print("Invalid Input, only choose from the selection (1/2/3) \n")
