"""
Create a program that ask user for a question, 
it will also ask for 4 possible answer (a,b,c,d)
and the correct answer. Write the collected data
to a text file. Ask another question until the
user chose to exit.

"""
import time

base_name = input("File name of quiz: ")

time_stamp = time.strftime("%d%m%Y_%H%M%S")

file_name = f"{base_name}_{time_stamp}.txt"

while True:
    #ask for inputs (question, possible answers, and correct answer)
    question = input("Enter a question: ")
    option_a = input("Enter option a: ")
    option_b = input("Enter option b: ")
    option_c = input("Enter option c: ")
    option_d = input("Enter option d: ")
    correct_answer = input("Enter Correct answer: ")

    #write the collected data to a .txt file
    with open(file_name,"a") as quiz_file:
        quiz_file.write("Question: " + question + "\n")
        quiz_file.write("A. " + option_a + "\n")
        quiz_file.write("B. " + option_b + "\n")
        quiz_file.write("C. " + option_c + "\n")
        quiz_file.write("D. " + option_d + "\n")
        quiz_file.write("Correct Answer: " + correct_answer + "\n")
        

    #keep looping until user chooses to exit the program
    input_another_question = input("Do you want to enter another question? (yes/no): ").strip().lower()
    if input_another_question[0] == 'n':
        print("Exiting.....")
        break