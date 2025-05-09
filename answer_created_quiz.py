"""
Create the Quiz program that read the output file of the Quiz Creator.
The user will answer the randomly selected question and check if the answer is correct.
"""
import os
import random

text_files = []
each_line = []

#find text files
for files_name in os.listdir("."):
    if files_name.endswith(".txt"):
        text_files.append(files_name)

#ask which file to open
number_counter = 0
for files in text_files:
    print(f"{str(number_counter + 1)}) {files}")
    number_counter += 1


selected_file = int(input("Enter which file you want to open: "))

#open text file
with open(text_files[selected_file - 1] , 'r') as quiz_file:
    for lines in quiz_file:
        each_line.append(lines)

#randomize questions/ if possible randomize options aswell

number_of_questions = len(each_line) // 6 #each question is composed of 6 lines 

randomizer = random.sample(range(1, number_of_questions + 1), number_of_questions)

for random_number in randomizer:
    index = (random_number - 1) * 6
    current_question = each_line[index:index + 5]
    for lines in current_question:
        print(lines, end = '')
    
    #get users answer
    answer = input("\nEnter Your Answer: ")

    #show if answer is correct
    current_answer = each_line[index+5][16:].strip().lower()
    if answer.lower().strip() == current_answer:
        print("correct")
    else:
        print("incorrect")


