import random

words=["movie", "books", "games", "songs" ]
print("Guess Julia is more intrested in {}".format(words))
word=random.choice(words)

while True:
    User=input("Enter your guess :")

    if User not in words:
        print("sorry Entered word is not in list, Try again")
        continue
    if User==word:
        print("your guess is right : {}".format(word))
        get=input("do you like to continue [y/n] :")
        if get=='y':
            word=random.choice(words)
            continue
        else:
            break
    else:
        print("Wrong Guess")
        continue
