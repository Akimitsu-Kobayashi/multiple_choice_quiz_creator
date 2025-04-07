"""
Create a program that ask user for a question, 
it will also ask for 4 possible answer (a,b,c,d)
and the correct answer. Write the collected data
to a text file. Ask another question until the
user chose to exit.

"""

while True:
    #ask for inputs (question, possible answers, and correct answer)
    question = input("Enter a question: ")
    option_a = input("Enter option a")
    option_b = input("Enter option b")
    option_c = input("Enter option c")
    option_d = input("Enter option d")
    correct_answer = input("Enter Correct answer")

    #write the collected data to a .txt file
    with open("question_and_answer.txt","a") as quiz_file:
        quiz_file.write(question + "\n")
        quiz_file.write(option_a + "\n")
        quiz_file.write(option_b + "\n")
        quiz_file.write(option_c + "\n")
        quiz_file.write(option_d + "\n")
        quiz_file.write(correct_answer + "\n")
        

    #keep looping until user chooses to exit the program
