from random import random
def human(number_of_mistakes):
    if number_of_mistakes == 0:
        print("You have full health")
    elif number_of_mistakes == 1:
        print("The hangman:")
        print("  o")


    elif number_of_mistakes == 2:
        print("The hangman:")
        print("  o")
        print("  |")
    elif number_of_mistakes == 3:
        print("The hangman:")
        print("  o")
        print("  | -")
    elif number_of_mistakes == 4:
        print("The hangman:")
        print("  o")
        print("- | -")
    elif number_of_mistakes == 5:
        print("The hangman:")
        print("  o")
        print("- | -")
        print(" |")
    elif number_of_mistakes == 6:
        print("The hangman:")
        print("  o")
        print("- | -")
        print(" | |")

def singers():
    x = int(random()*10)
    while x > 5 or x<1:
        x = int(random() * 10)
    if x == 0:
        return ("Koby Oz")
    if x == 1:
        return ("Miley Syrus")
    if x == 2:
        return ("Kanye West")
    if x == 3:
        return ("Moshe Peretz")
    if x == 4:
        return ("Gidi Gov")

def capitals():
    x = int(random()*10)
    while x > 5 or x<1:
        x = int(random() * 10)
    if x == 1:
         return str("Washington")
    if x == 2:
        return str("Budapest")
    if x == 3:
        return str("Beijing")
    if x == 4:
        return str("Amsterdam")
    if x == 5:
        return str("Jerusalem")

def beers():
    x = int(random()*10)
    while x > 5 or x<1:
        x = int(random() * 10)
    if x == 0:
        return ("Carlsberg")
    if x == 1:
        return ("Weinstephen")
    if x == 2:
        return ("Hobgarden")
    if x == 3:
        return (" Corona")
    if x == 4:
        return ("Maccabi")

def guessing(origin_word, word_string):
    life = 0
    word_counter = 0
    word_string = list(word_string)
    origin_word_check = origin_word
    origin_word = list(origin_word)
    guest_letters = ""

    while word_counter < len(origin_word):
        check_counter_letter = False
        print("")
        print("")
        guessing_letter = input("Enter a word here:        ")
        while guessing_letter.isalpha() == False or guessing_letter in guest_letters or len(guessing_letter) != 1:  # וידוא של הקלט
              guessing_letter = input("Enter a word here(not one you have all ready tried):")
        print("")
        print("")

        guest_letters += guessing_letter+","  # שמירת האותיות שכבר נוסו

        for i in range(len(origin_word)):
            if guessing_letter == origin_word[i]: # אם האות נמצאת במילה
               word_string[i] = str(guessing_letter)
               check_counter_letter = True
               word_counter += 1

        if check_counter_letter == True:
            print("The word to guess:", ''.join(word_string), "      Letters you have all ready guessed:", guest_letters), human(life)

        if word_counter == len(origin_word) or word_counter == len(origin_word)-1:
              string_ending = ""
              for i in range((len(origin_word))):
                  string_ending += origin_word[i]
              if string_ending == origin_word_check:
                  return ("Corect!!", "The word is:", ''.join(origin_word, human(life)))


        if check_counter_letter == False:   # אם האות לא נמצאת במילה
           life += 1

           if life == 6:
              return ("You have lost!","The word was:",origin_word)


           else:
             print("    ","The word to guess:",''.join(word_string),"      Letters you have all ready guessed:",guest_letters),human(life)






print("Welcome to Hangman!                                                 ")
print("")
print("Choose on of the follow options:                                            ")
print("1) Singers     2)Capital cities     3) Names of beers     ")
category = input("Enter here the number of the category:                       ")
while (category != str(1)) and (category != str(2)) and (category != str(3)) :
     print("")
     print("Choose a number between 1-3")
     print("")
     print("1) Singers     2) Capital cities   3) Names of beers      ")
     category = input("Enter here the number of the category:                                    ")

if category == str(1):
    word = singers()
elif category == str(2):
    word =capitals()
elif category == str(3):
    word =beers()

origin_word = word
word = list(word)
for i in range(len(word)):
    if word[i] != " ":
        word[i] = "_"
    else:
        word[i] = "-"
word_string=""
for i in range(len(word)):
    word_string += word[i]
print("")
print("The word to guess:        ")
print(word_string)
print(guessing(origin_word,word_string)),human(6)









