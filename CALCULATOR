#IMPORTS
import sys
import random
#VARIABLES
count = 0
#FUNCTIONS
def leave(what):
	sys.exit(what)

print("I will try to crack your code of 4 digits(make sure it's bigger than 1111).")
digits = (int(input("\nHow many digits do you want?")))
if digits > 5:
	print("\nThis program doesn't accept that many digits as of now.")
	print(leave("\n---\nTOO MANY DIGITS\n---"))
elif digits < 4:
	print("\nThis program doesn't less than 4 digits as of now.")
	print(leave("\n---\nTOO LITTLE DIGITS\n---"))
else:
	pass
code = (int(input("\nWhat is the code you want me to crack, I won't look.")))
if code > 9999999:
	print("\nYou put more digits than you said you would. Try again")
	sys.exit("\n--\nToo many digits\n---")
elif code < 1111111:
	print("\nYou put less digits than you said you would. Try again")
	sys.exit("\n---\nNot enough digits\n---")
else:
	pass
bet = (int(input("\nHow many guesses are you going to give me? If I win, you'll pay.")))
print("\nI'm going to try to guess your code right now. Here goes nothing.")
guess = (int(random.randint(1111111, 9999999)))
if guess == code:
	print("Wow, I guessed it in one try. here's the number I guessed -")
	print(guess)
	print("Here's the number you put -")
	print(code)
else:
	pass
while guess!=code:
	count += 1
	if count == 10 or 20 or 30 or 40 or 50 or 60 or 70 or 80 or 90 or 100:
		print("I'm on my " + (str(count)) + " attempt")
	else:
		pass
	if count == bet:
		print("\nOK, you won, I didn't guess it int time. BYE")
		break
	else:
		pass
	guess = (int(random.randint(1111111, 9999999)))
	if guess == code:
		print("Wow, I got it! I did it! I guessed your number! Just to check, your number is " + (str(code)) + "\nAnd my number is " + (str(code)) + "I did it, didn't I?!")
		break
	else:
		pass
