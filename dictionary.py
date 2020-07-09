#create a cinema simulator which checks if there is a seat available for 
#the movie they want to watch
# create a dictionary to hold the movie name, number of seats, avlb seats
movies={"Frozen":[3,5],"Finding Dory":[3,1], "Jungle Book":[10,7],"Gravity":[10,6],"Gone Girl":[18,10]}
import time
while True:
	choice= input("Which movie would you like to watch?: ").strip().title()

	if choice in movies:
		age=int(input("How old are you?: ").strip())
		if age >=  movies[choice][0]:
			print("Let me check the availability...")
			time.sleep(5)
			if (movies[choice][1]>=1):
				movies[choice][1]=movies[choice][1]-1 
				print("Voila!Seats available!,Enjoy your movie!")
			else:
				print("Sorry, we are sold out")

		else:
			print("You are not eligible")
			

	else:
		print("We dont have that movie..")


