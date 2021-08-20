#this program is a password generator

import random #library for random functions

password_list = [] #list to hold characters within password

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o','p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 
    'F', 'G', 'H','I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
    'W', 'X', 'Y', 'Z']#list to hold letters of Alphabet

numbers = ['1','2','3','4','5','6','7','8','9','0'] #list to hold numbers for password generation
symbols = ['!','#', '$', '%', '&', '(', ')', '*', '+'] #list to hold special characters for password generation

print("Welcome to Random Password Generator!\n")

lettersAmount = int(input("How many letters would you like in your password?:"))
numbersAmount = int(input("How many numbers would you like in your password?:"))
symbolsAmount = int(input("How many symbols would you like in your password?:"))

#loop to add letters to list
for letters in range(lettersAmount):
    temp = random.choice(alphabet)
    password_list.append(temp)

    #loop to get numbers for password
for number in range(numbersAmount):
    temp = random.choice(numbers)
    password_list.append(temp)

#loop to get symbols for password
for symbol in range(symbolsAmount):
    temp = random.choice(symbols)
    password_list.append(temp)

random.shuffle(password_list)

password = ""

for characters in password_list:
    password += characters

print(f"Your new randomized password is: {password}")

input("Press enter to exit the program")

    