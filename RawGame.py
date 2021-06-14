#making a Number The Number Game
import random

def start_game():
	attempt = 1
	max_attempt = 5
	score = 100
	random_number = random.randint(1,10)
	print("Welcome To The Game Of Guessing The Number")
	name = input("Enter Your Name:")
	print(' Hello ' +  name )
	score -= 20
	max_attempt -= 1
		#To print random number by the computer
	random_number = random.randint(1,10)
	print("Welcome To The Game Of Guessing The Number")
	#username


	while attempt <= max_attempt:
		number_guess = int(input(" Choose A Number Between 1 to 10: "))
		
		if int(number_guess <= 0 or number_guess > 10):
			print('Invalid Number Please input a random number between 1 to 10')
		if (number_guess == random_number):
			print('Congratulations You Have Guessed The Correct Number')
			break
		if number_guess < random_number:
			print('The number should be higher')
		else:
			print('The number should be lower')
	#For the odd numbers in range of 1 to 10 (range(start,stop),step)
		if ((max_attempt == 4) and (random_number % 2) != 0): 
			print('The number is an odd number')
		
		elif ((max_attempt == 4) and (random_number % 2) == 0):
			print('The number is an even number')
			
		
		#For the Third Attempt
		elif ((max_attempt == 3) and (random_number % 3 == 0 )):
			print('The number is an multiples of 3')
		elif ((max_attempt == 3) and (random_number % 3 != 0 )):
			print('The number not in the multiples of 3')
		
		#For the Third Attempt
		elif ((max_attempt == 2) and (random_number % 4 == 0 )):
			print('The number is an multiples of 4')
		elif ((max_attempt == 2) and (random_number % 4 != 0 )):
			print('The number not in the multiples of 4')
		
		#For the Third Attempt
		elif ((max_attempt == 1) and (random_number % 5 == 0 )):
			print('The number is an multiples of 5')
		elif ((max_attempt == 1) and (random_number % 5 != 0 )):
			print('The number not in the multiples of 5')	
		

		#We do a for loop 
		if (number_guess == random_number):
			print('Your Current Score is' ,score,"%" )
		else:
			score -= 20
			max_attempt -=1
			print('Your Current Score is' ,score,"%")
			print('Number of attempts remaining',max_attempt)
	if max_attempt == 0:
		print("Game Over The Random Number is",random_number),
		return




		#To allow the user to insert input multiple times
		#Decrease the number of attempts
		
		#To include scoring inside the game
		
	
start_game()