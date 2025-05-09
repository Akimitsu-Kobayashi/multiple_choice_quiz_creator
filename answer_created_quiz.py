"""
Create the Quiz program that read the output file of the Quiz Creator.
The user will answer the randomly selected question and check if the answer is correct.
"""
import os
import random
import pyfiglet
from termcolor import colored

title = pyfiglet.figlet_format("Welcome to \n Answer Quiz")
print(colored(title, "blue"))

text_files = []
each_line = []
total_score = 0

#find text files
for files_name in os.listdir("."):
    if files_name.endswith(".txt"):
        text_files.append(files_name)

#ask which file to open
number_counter = 0
for files in text_files:
    print(f"{str(number_counter + 1)}) {files}")
    number_counter += 1

while True:
    try:
        selected_file = int(input("Enter which file you want to open: "))
        if 0 < selected_file <= len(text_files):
            break
        else:
            print(colored("Error: Number Out of Range", "red"))
    except:
        print(colored("Error: The Input is not a number", "red"))

print("\n")

#open text file
with open(text_files[selected_file - 1] , 'r') as quiz_file:
    for lines in quiz_file:
        each_line.append(lines)

#each question is composed of 6 lines
number_of_questions = len(each_line) // 6 

#randomize questions
randomizer = random.sample(range(1, number_of_questions + 1), number_of_questions)

for random_number in randomizer:
    index = (random_number - 1) * 6
    current_question = each_line[index:index + 5]

    for lines in current_question:
        print(lines, end = '')
    #get users answer
    while True:
        try:
            answer = input("\nEnter Your Answer: ")
            if answer.lower().strip() not in ['a', 'b', 'c', 'd']:
                print(colored("Invalid Input possible answers are only (a/b/c/d)", "red"))
            else:
                break
        except:
            print(colored("Invalid Input possible answers are only (a/b/c/d)", "red"))
    
    #show if answer is correct
    current_answer = each_line[index+5][16:].strip().lower()
    if answer.lower().strip() == current_answer:
        print(colored("correct\n", "green"))
        total_score += 1

    else:
        print(colored("incorrect\n", "red"))

#show red if failed and green if pass
grade = round((total_score / number_of_questions) * 100, 2)

print("Average Score: ", end = '')

if 25 <= grade <= 70:
    print(colored(grade, "yellow"))
elif 0 == grade < 25:
    print(colored(grade, "red")) 
else:
    print(colored(grade, "green"))