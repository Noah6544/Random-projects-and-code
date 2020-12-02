import random
import sys

print("HEY, WANNA PLAY? ALL IT TAKES IS A LITTLE PART OF\n YOUR DAY!\nENTER A NUMBER 1-100 IF YOU GUESS RIGHT,\n YOU\'RE THE BEST!\nREADY TO PUT IT TO THE TEST?")
main = (str(input("\nWould you rather try to guess 1 number - you can have a certain amount of guesses - or spam other? Press 1 for one number and 2 for spam - type \"quit\" at anytime to see the answer - ")))
"""
if main != "1" or  main != "2":
  print("\nINVALID INPUT")
  sys.exit()
else:
  pass
"""
count = 0
if main == "1":
  value=(int(random.randint(1,100)))
  print(value)
  print("\nOne number? Cool, I think that's more fun anyways.")
	#bet = input("\nHow many guesses do you want?")
  guess=(int(input("\nWhat's your guess?! - ")))  
  while guess != value:
		if guess > value:
			print("Too high...")
		elif guess < value:
    	print("Too low...")
    elif guess == (int("quit")):
    	print("Giving up so soon? The winning  number was - " + (str(value)) + "BETTER LUCK NEXT TIME!")  
	elif guess == bet:
		print("\nYou ran out of guesses, better luck next time!") 
		print("")
		break
	elif guess == value:
  	break
    guess=(int(input("\nWhat's your guess?! - ")))  
    count += 1
  elif guess==value:    
  	print("WOW, YOU GOT IT - THE NUMBER WAS - " + (str(value)) + "TEST")
else:
  guess=(int(input("\nWhat's your guess?! - ")))
  value=(int(random.randint(1,100)))
  if guess=='right':
    print("\nYOU FOUND THE EASTER EGG!!!!")
		break
  elif guess>value:
    print("Your guess is too high, try again.")
  else:
    while guess!=value:
      print("\nTHE WINNING NUMBER WAS: " + value)
      print("\YOU GUESSED IT - " + (str(guess)))
			print("")
			break 
      guess=(int(input("\nWhat's your guess? - ")))
      value=(int(random.randint(1,100)))
      if guess == value:
        print("WOW, YOU WON!")
				print("")
        break
      elif guess=='right':
        print("\nYOU FOUND THE EASTER EGG!!!!")
        print("")
        break
      elif guess > value and guess != value:
        print("Your guess is too high, try again.")
    else:
      print("Your broke it bum.")
     
