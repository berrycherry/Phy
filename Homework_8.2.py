secret=23
guess=int(input("What is the secret number? "))
if guess==secret:
    print("Congratulations you guessed the secret number.")
else:
    print(guess+" is not the secret number. Try again!")