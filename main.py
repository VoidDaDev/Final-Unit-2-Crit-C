"""
Coded by: Lysandre Roussianos / 22.11.2022

This program is developed for any teachers/organisation,
who needs to write down their students grades,
and get their final grade.
"""
import os
from colorama import Fore, Back, Style

# Login credentials
username = "Isl123"
password = "Isl2k22"

# A function created for the title, easier to set it inside a function so we don't have to print it everytime.
def title():
    print("""
 _____               _ _              ______                                    
|  __ \             | (_)             | ___ \                                   
| |  \/_ __ __ _  __| |_ _ __   __ _  | |_/ / __ ___   __ _ _ __ __ _ _ __ ___  
| | __| '__/ _` |/ _` | | '_ \ / _` | |  __/ '__/ _ \ / _` | '__/ _` | '_ ` _ \ 
| |_\ \ | | (_| | (_| | | | | | (_| | | |  | | | (_) | (_| | | | (_| | | | | | |
 \____/_|  \__,_|\__,_|_|_| |_|\__, | \_|  |_|  \___/ \__, |_|  \__,_|_| |_| |_|
                                __/ |                  __/ |                    
                               |___/                  |___/                     """)


# Login function created in order for the user to connect onto the program,
# There is a loop that keep asking for the credentials if they are wrong.
def login_menu():
    title()
    while True:
        try:
            user_name = str(input(Fore.GREEN + "Username: "))
            break
        except ValueError:
            print(Back.RED + "Only input letters")
    while True:
        try:
            pass_word = str(input(Fore.GREEN + "Password: "))
            break
        except ValueError:
            print(Back.RED + "Only input letters")

    while user_name != username or pass_word != password:
        print(Style.RESET_ALL)
        print(Fore.RED + "Wrong Login Credentials.")
        print(Style.RESET_ALL)
        user_name = input(Fore.GREEN + "Username: ")
        pass_word = input(Fore.GREEN + "Password: ")
    os.system("clear")
    print(Style.RESET_ALL)
    main_menu()

# Function created to check if user input is only containing positive integers
def checkint(question):
    while True:
        try:
            ans = int(input(question))
            if ans >= 0:
                return ans
        except ValueError:
            print(Fore.RED + "Only input positive numbers")
            print(Style.RESET_ALL)


# Main menu function created for the user to be able to select between options 1, 2 or 3.
def main_menu():
    while True:
        title()
        print("\n")
        print("1 - Test Assessment")
        print("2 - MYP Assessment")
        print("3 - Exit")
        user_choice = checkint(Fore.CYAN + "\n > ")
        if user_choice == int(1):
            os.system("clear")
            print(Style.RESET_ALL)
            test_assessment()
        elif user_choice == int(2):
            os.system("clear")
            print(Style.RESET_ALL)
            myp_assessment()
        elif user_choice == int(3):
            print("Goodbye!")
            os.system("clear")
            break
        else:
            print("Invalid Selection.")
            input("Press [ENTER] to continue")
            os.system("clear")
            print(Style.RESET_ALL)


# Function created in order to receive the final grade for a test assessment
def test_assessment():
        title()
        # loop created in order to verify if the input of the users is corresponding to a string
        while True:
            try:
                stud_name = str(input("Student Name: "))
                break
            except ValueError:
                print("Only input letters")
                #At line 106 we can see the usage of the function checkint
        max_score = checkint("Maximum Test Score: ")
        stud_score = checkint("Student Score: ")
        while stud_score > max_score:
            print("The student score cannot be above the maximum score.")
            max_score = checkint("Maximum Test Score: ")
            stud_score = checkint("Student Score: ")
        test_result = round((stud_score / max_score) * 100, 1)
        print("Final Percentage of " + stud_name + ": " + str(test_result) + "%")
        if test_result >= 90:
            print("Final Test Grade: 8")
        elif test_result >= 80:
            print("Final Test Grade 7")
        elif test_result >= 70:
            print("Final Test Grade: 6")
        elif test_result >= 60:
            print("Final Test Grade: 5")
        elif test_result >= 50:
            print("Final Test Grade: 4")
        elif test_result >= 40:
            print("Final Test Grade: 3")
        elif test_result >= 30:
            print("Final Test Grade: 2")
        elif test_result < 30:
            print("Final Test Grade: 1")
        print("\n")
        input(Fore.GREEN + "Press [ENTER] to go back to the main menu")
        print(Style.RESET_ALL)
        os.system("clear")
        

# Function created in order to let the client use myp assessment grading section
def myp_assessment():
        title()
        while True:
            try:
                stud_name = input("Student Name: ")
                break
            except ValueError:
                print("Only input letters")

        crit_a = checkint("Criterion A: ")
        while crit_a > 8 or crit_a < 0:
                print("Only input numbers between 0-8")
                crit_a = checkint("Re enter Criterion A: ")
        crit_b = checkint("Criterion B: ")
        crit_c = checkint("Criterion C: ")
        crit_d = checkint("Criterion D: ")

        # Using the function round(in order to not deal with uneccesary decimals and round it to nearest 1 d.p)
        test_result = round(crit_a + crit_b + crit_c + crit_d, 1)
        if test_result >= 28:
            print("Final MYP Grade: 7")
        elif test_result >= 24:
            print("Final MYP Grade 6")
        elif test_result >= 19:
            print("Final MYP Grade: 5")
        elif test_result >= 15:
            print("Final MYP Grade: 4")
        elif test_result >= 10:
            print("Final MYP Grade: 3")
        elif test_result >= 6:
            print("Final MYP Grade: 2")
        elif test_result >= 1:
            print("Final MYP Grade: 1")
        elif test_result < 1:
            print("Final MYP Grade: 0")
        print("\n")
        input(Fore.GREEN + "Press [ENTER] to go back to the main menu")
        print(Style.RESET_ALL)
        os.system("clear")

# A simple calling of the function login_menu to start the app
login_menu()
