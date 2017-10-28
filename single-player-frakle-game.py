import random

def getChoice(prompt, validChoices):
    # Repeatedly prompt the user for input until they enter one of the valid choices
	print prompt
	text = validChoices[0]
	if len(validChoices) > 1:
		for c in range(1, len(validChoices)):
			text += ' or "' + validChoices[c] + '"'
	user_choice = None
	while not user_choice in validChoices:
		user_choice = input("Enter " + text + ": ")
	return user_choice

# Set score to 0 and print a welcome message
score = 0
print "Starting game!"

# Loop 3 times, setting the 'turn' variable to 1, then 2, then 3
for turn in range(1, 4):
	print "Turn " + str(turn) + " of 3"
	print "Current Score" + str(score)

    # Reset remaining dice and points for current turn
	points = 0
	dices_to_roll = 6

    # Set rollAgain to True at start of each turn
    # This will be set to False if the user chooses not to roll again or if they can't/don't set any dice aside
    rollAgain = True

    # Loop while rollAgain is True
    while rollAgain:

        # Roll remaining dice
		print "Rolling " + str(dices_to_roll) + " dice."
		dices = []
		for dice in range(1, dices_to_roll+1):
			dices.append( random.randint(1, 6) )
		print "Rolled " + str(dices)

        # Set nothingStored to True before checking for matching numbers
        # This will be set to False if the user sets dice aside
        nothingStored = True

        # Loop 6 times, setting the 'num' variable to each number between 1 and 6
        for num in range(1, 7):
            # Find matching dice and prompt user to set them aside
            # (nothingStored will be set to False if the user puts dice aside in this part)
			matches = len( [i for i,x in enumerate(dices) if x==num] )

			if matches > 1:
				match_points = matches * num
				msg = str(matches) + " x " + str(num) + " rolled, worth " + str(match_points) + " points. Set aside these dice?"
				user_choice = getChoice(msg, ["yes", "no"])
				if user_choice == "yes":
					nothingStored = False
					points = points + match_points
					dices_to_roll = dices_to_roll - matches
					print "Setting aside " + str(matches) + " x " + str(num) + " for " + str(match_points) + " points."

        # If no dice set aside
        if nothingStored:
            # End turn by setting rollAgain to False and don't add points to score
            rollAgain = False
			print "No dice set aside - turn over! " + str(points) + " points lost!"

        else:
            # Ask user whether they want to roll again or end turn
            # rollAgain will get set to False if they choose to end their turn, and the turn's points will be added to their score
			msg = "You have " + str(dices_to_roll) + " dice remaining and " + str(points) + " points on the line. Roll remaining dice or end turn to secure points?"
            user_choice = getChoice(msg, ["roll", "end"])

			if user_choice == "end":
				score = score + points
				rollAgain = False
				print str(points) + " points secured."

# Show end of game messages
print "Game over. Final score: " + str(score) + "."
