"""
Create the Quiz program that read the output file of the Quiz Creator.
The user will answer the randomly selected question and check if the answer is correct.
"""
import os

text_files = []

#open file 
for files_name in os.listdir("."):
    if files_name.endswith(".txt"):
        text_files.append(files_name)

#ask which file to open
number_counter = 0
for files in text_files:
    print(f"{str(number_counter + 1)}) {files}")
    number_counter += 1


selected_file = int(input("Enter which file you want to open: "))


#randomize questions/ if possible randomize options aswell

#show if answer is correct

#loop until there is no more questions

