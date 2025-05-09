"""
Create the Quiz program that read the output file of the Quiz Creator.
The user will answer the randomly selected question and check if the answer is correct.
"""
import os

#open file 
for files_name in os.listdir("."):
    if files_name.endswith(".txt"):
        print(files_name)

#randomize questions/ if possible randomize options aswell

#show if answer is correct

#loop until there is no more questions

