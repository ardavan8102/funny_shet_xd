from random import choice
from enchant import Dict

dictionary = Dict('en_US')

letters = [
    'a', 'b', 'c',
    'd', 'e', 'f',
    'g', 'h', 'i',
    'j', 'k', 'l',
    'm', 'n', 'o',
    'p', 'q', 'r',
    's', 't', 'u',
    'v', 'w', 'x',
    'y', 'z'
]

start_letter = input("Word Will Starts With : ")
word_lenght = int(input("Lenght Of Word : "))

print()
print(start_letter, end = "")

word = ""

for i in range(word_lenght - 1):
    get_letter = choice(letters)
    word += get_letter

print(word)
print(dictionary.check(word)) # Check Word Is Meaningful or not

input("\nPress ENTER To Exit") # Quit The Program