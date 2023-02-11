"""
slama_projekt.py: první projekt do Engeto Online Python Akademie
author: David Sláma
email: cimka1@seznam.cz
discord: cimka1#2497
"""

seperator = "----------------------------------------"

users = {'bob': '123', 'ann': 'pass123', 
'mike': 'password123', 'liz': 'pass123'}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user_name = input("username: ")
password = input("password: ")


def pocetslov():
    count_of_words = len(TEXTS[int(choice) - 1].split())
    print("There are ", count_of_words, " words in the selected text.")

def velkepismeno():
    pocet = 0
    for word in TEXTS[int(choice) - 1].split():
        if word[0].isupper():
         pocet = pocet + 1
    print("There are ", pocet, "titlecase words.")

def pocetcislic():
    pocet = 0
    for word in TEXTS[int(choice) - 1].split():
        if word.isdigit():
            pocet = pocet + 1
    print("There are ", pocet, "numeric strings")

def vsechnyvelka():
    pocet = 0
    for word in TEXTS[int(choice) - 1].split():
        if word.isupper() and word[0].isalpha():
         pocet = pocet + 1                         
    print("There are ", pocet, "uppercase words.")

def vsechnymala():
    pocet = 0
    for word in TEXTS[int(choice) - 1].split():
        if word.islower():
         pocet = pocet + 1                        
    print("There are ", pocet, "lowercase words.")

def sumacislic():
    vysledek = 0
    for word in TEXTS[int(choice) - 1].split():
        if word.isdigit():
            vysledek += int(word)
    print("The sum of all the numbers", vysledek)

def graf():
    word_lengths={}
    for word in TEXTS[int(choice)-1].split():
        if word.isalpha():
            if len (word) in word_lengths:
                word_lengths[len(word)]+=1
            else:
                word_lengths[len(word)] = 1
        word_lengths = dict(sorted(word_lengths.items()))
    for length, count in word_lengths.items():
        print(f"{length:2d}|{'*'*count:<15}{count}")





if users.get(user_name) == password:
    print(seperator,
    "Welcome to the app", user_name, 
    "We have 3 texts to be analyzed.",
    seperator,
    sep="\n")
 
    choice = input("Enter a number btw. 1 and 3 to select: ")
    pocetslov()
    velkepismeno()
    pocetcislic()
    vsechnyvelka()
    vsechnymala()
    sumacislic()
    graf()
    print("-" * 30)
    print("LEN |    OCCURENCES  |   NR")
    print("-" * 30)
else:
    print("Špatné jméno nebo heslo..")

