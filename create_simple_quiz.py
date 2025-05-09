"""
Create a program that ask user for a question, 
it will also ask for 4 possible answer (a,b,c,d)
and the correct answer. Write the collected data
to a text file. Ask another question until the
user chose to exit.

"""
import time
import os
import pyfiglet
from termcolor import colored

base_name = input("File name of quiz: ")
time_stamp = time.strftime("%d%m%Y_%H%M%S")
file_name = f"{base_name}_{time_stamp}.txt"

question_number = 1
questions_made = 0

title = pyfiglet.figlet_format("Welcome to \n QUIZ MAKER")
print(colored(title, "blue"))

def add_question():
    global file_name
    global question_number
    global questions_made
     #ask for inputs (question, possible answers, and correct answer)
    question = input("Enter a question: ").strip()
    option_a = input("Enter option a: ").strip()
    option_b = input("Enter option b: ").strip()
    option_c = input("Enter option c: ").strip()
    option_d = input("Enter option d: ").strip()
    while True:
        correct_answer = input("Enter Correct answer (a/b/c/d): ").strip().lower()
        if correct_answer in ['a', 'b', 'c', 'd']:
            break
        print(colored("Invalid Correct answer choose between (a/b/c/d)", "red"))


    #write the collected data to a .txt file
    with open(file_name, "a") as quiz_file:
        quiz_file.write(f"{question_number}.Question: {question}\n")
        quiz_file.write("A. " + option_a + "\n")
        quiz_file.write("B. " + option_b + "\n")
        quiz_file.write("C. " + option_c + "\n")
        quiz_file.write("D. " + option_d + "\n")
        quiz_file.write("Correct Answer: " + correct_answer + "\n\n")
        
    
    question_number += 1
    questions_made += 1

def view_questions():
    global file_name
    #read the file 
    if not os.path.exists(file_name):
        print(colored("no question saved yet.\n", "red"))
        return
        
    print(colored("contents of current file:", "green"))
    with open(file_name, "r") as quiz_file:
        print(quiz_file.read())

def edit_question():
    global file_name
    global questions_made
    lines = []

    #read the file 
    if not os.path.exists(file_name):
        print(colored("no question saved yet.\n", "red"))
        return
    
    with open(file_name, "r") as quiz_file:
        for line in quiz_file:
            lines.append(line)

    for number in range(questions_made):
        print(colored(f"Question {str(number + 1)}. \n", "green"))

    while True:
        try:
            number_to_edit = int(input("Number to Edit: ").strip())

            if 0 < number_to_edit <= questions_made:
                break
            else:
                print(colored(f"Number Out of range there are only {questions_made} questions saved", "red"))
            
        except:
            print(colored("Invalid Input", "red"))

    #so that the input of user corresponds to 0,7,14 and so one which is the separation of each questions
    index = (number_to_edit - 1)*7

    new_question = input("Enter a question: ").strip()
    new_option_a = input("Enter option a: ").strip()
    new_option_b = input("Enter option b: ").strip()
    new_option_c = input("Enter option c: ").strip()
    new_option_d = input("Enter option d: ").strip()
    while True:
        new_correct_answer = input("Enter Correct answer (a/b/c/d): ").strip().lower()
        if new_correct_answer in ['a', 'b', 'c', 'd']:
            break
        print(colored("Invalid Correct answer choose between (a/b/c/d)", "red"))


    #every question is 7 lines long
    lines[index] = f"{number_to_edit}.Question: {new_question}\n"
    lines[index + 1] = f"A. {new_option_a}\n"
    lines[index + 2] = f"B. {new_option_b}\n"
    lines[index + 3] = f"C. {new_option_c}\n"
    lines[index + 4] = f"D. {new_option_d}\n"
    lines[index + 5] = f"Correct Answer: {new_correct_answer}"
    lines[index + 6] = "\n\n"

    with open(file_name, "w") as quiz_file:
        quiz_file.writelines(lines)

while True:
    print(colored("\nQUIZ BUILDER MENU", "yellow"))
    print("1. Add a new question")
    print("2. View saved questions")
    print("3. Edit question")
    print("4. Exit")

    choice = input(colored("Select option (1/2/3/4): ", "blue")).strip()
    print("")

    if choice == '1':
        add_question()
    elif choice == '2':
        view_questions()
    elif choice == '3':
        edit_question()
    elif choice == '4':
        print("Goodbye")
        break
    else:
        print(colored("Invalid Input, only choose from the selection (1/2/3/4) \n", "red"))
