number = 23
guess = int(input('Enter an integer : '))

if guess == number:
	print('Congratulations, you guessed it.')
	print("(but you do not win any prizes!)")
elif guess < number:
	print("No, it is a little higher than that!")
else:
	print("No, it is a little lower than that")
	
print("Done.")

number2 = 23
running = True

while running:
	guess = int(input("Enter an integer: "))
	
	if guess == number2:
		print("Congratulations, you guessed it:")
		running = False
	elif guess < number2:
		print("No, it is a little higher than that")
	else:
		print("No, it is a little lower than that.")
else:
	print("The whole loop is over!")


print("Done")

	