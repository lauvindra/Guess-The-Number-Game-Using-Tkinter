#making a Number Guessing Game
import random
import tkinter as tk


window = tk.Tk()
window.title("Guess The Number")
window.geometry("480x240")

#To add background picture




#Labelling the window
lblIntro = tk.Label(window, text = "Welcome To The Game of Guess the number" '\n' "Guess a number from 1 to 10")
lblLine0 = tk.Label(window, text = "---------------------------------------------------------------------")


lblNoGuess = tk.Label(window, text = "No of Guesses: 0")
lblMaxGuess = tk.Label(window, text = "Max Guess: 5")
lblLine1 = tk.Label(window, text = "---------------------------------------------------------------------")
lblLogs = tk.Label(window, text=" ") 
lblLine2 = tk.Label(window, text = "---------------------------------------------------------------------")


#Create Buttons
buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index : main_game(index), state=tk.DISABLED)
    buttons.append(button)
#for the start button the index starts from 0
btnStartGameList = []
btnStartGame = tk.Button(window, text="Start Game", command=lambda : start_game(0))
btnStartGameList.append(btnStartGame)


#Positioning of the text window
lblIntro.grid(row=0, column=0, columnspan=5)
lblLine0.grid (row=1, column=0, columnspan=5)
lblNoGuess.grid(row=2, column=0, columnspan=3) 
lblMaxGuess.grid(row=2, column=3, columnspan=2)
lblLine1.grid(row=3, column=0, columnspan=5) 
lblLogs.grid(row=4, column=0, columnspan=5)

lblLine2.grid(row=9, column=0, columnspan=5)


for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col)

btnStartGameList[0].grid(row=13, column=0, columnspan=5)

#Main Game Logic
attempt = 0
max_attempt = 0
random_number = random.randint(0,9)
lblLogs = []
guess_row = 4



def init():
	global buttons, attempt, max_attempt, random_number, lblNoGuess, lblLogs, guess_row
	attempt = 0
	max_attempt = 0
	random_number = random.randint(0,9)
	print(random_number)
	lblNoGuess["text"] = "Number of Guesses: 0"
	guess_row = 4

    # Remove the data after clicking restart
	for lblLog in lblLogs:
		lblLog.grid_forget()
	lblLogs = []


def main_game(i):
	
	global max_attempt, buttons, guess_row
	attempt = i
	
	max_attempt += 1
	lblNoGuess["text"] = "Number of Guesses: " + str(max_attempt)
	


#username	
#User input
	#To print random number by the computer
	if (attempt == random_number):
		lbl = tk.Label(window, text ="Congratulations You Have Guessed The Correct Number" + str (random_number),fg="green")
		lbl.grid(row=guess_row, column=0, columnspan=5)
		lblLogs.append(lbl)
		guess_row += 1

		for b in buttons:
			b["state"] = tk.DISABLED

	else:
		#First Attempt.
		if (max_attempt == 1):
			if (attempt < random_number):
				lbl = tk.Label(window, text = "The number should be higher" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number should be higher')
			else:
				lbl = tk.Label(window, text = "The number should be lower" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number should be lower')
		
		#For the odd numbers in range of 1 to 10 (range(start,stop),step)
		#For the Second Attempt
		
		elif (max_attempt == 2):
			
			if (random_number % 2 != 0):  
				lbl = tk.Label(window, text = "The number is an odd number" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number is an odd number')
		
			else:
				lbl = tk.Label(window, text = "The number is an even number" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number is an even number')
	
				
		#For the Third Attemp
		elif (max_attempt == 3):

			if (random_number % 3 == 0 ):
				lbl = tk.Label(window, text = "The number is an multiples of 3" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number is an multiples of 3')
			else:
				lbl = tk.Label(window, text = "The number not in the multiples of 3" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number not in the multiples of 3')
				
		#For the Third Attempt
		elif (max_attempt == 4):

			if(random_number % 4 == 0 ):
				lbl = tk.Label(window, text = "The number is an multiples of 4" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number is an multiples of 4')
			else:
				lbl = tk.Label(window, text = "The number not in the multiples of 4" ,fg="red")
				lbl.grid(row=guess_row, column=0, columnspan=5)
				lblLogs.append(lbl)
				guess_row += 1
				print('The number not in the multiples of 4')
				

#For the odd numbers in range of 1 to 10 (range(start,stop),step)
	#To include scoring inside the game
	#We do a for loop 

	if max_attempt == 5:
		if attempt != random_number:
			lbl = tk.Label(window, text="Max guesses reached.Try Again)", fg="red")
			lbl.grid(row=guess_row, column=0, columnspan=5)
			lblLogs.append(lbl)
			guess_row += 1
	
		for b in buttons:
			b["state"] = tk.DISABLED

	buttons[i]["state"] = tk.DISABLED


status = "none"		

#To make the restart to clear
def start_game(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        btnStartGameList[i]["text"] = "Restart Game"
    else:
        status = "restarted"
        init()
    print("Game started")


window.mainloop()
