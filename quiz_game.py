print ("Welome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() !="yes":
	quit()

print("Okay! let's play :)")
score = 0

answer= input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
	print('Correct!')
	score +=1
else:
	print("Incorrect!")

answer= input("What does ALU stand for? ")
if answer.lower() == "arithmetic logic unit":
	print('Correct!')
	score +=1
else:
	print("Incorrect!")

answer= input("What does ROM stand for? ")
if answer.lower() == "read only memory":
	print('Correct!')
	score +=1
else:
	print("Incorrect!")

answer= input("What does P-O-S-T stand for? ")
if answer.lower() == "power on self test":
	print('Correct!')
	score +=1
else:
	print("Incorrect!")

answer= input("Which language computer understand? ")
if answer.lower() == "binary":
	print('Correct!')
	score +=1
else:
	print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You scored " + str((score/4)*100) + "%")