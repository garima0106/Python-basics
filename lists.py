known_users=['Alice', 'Bob', 'Harry', 'John','George', 'Peppa', 'Niki','Kia', 'Myra']
print(len(known_users))

while True:
	print('Hi My name is Travis! I am your security Bot')

	name=input("What's your name?: ").strip().capitalize()

	if name in known_users:
		print('Hello {}!'.format(name))
		remove=input('Would you like to be removed from the system[y/n]?: ').strip().lower()
		if remove=='y':
			known_users.remove(name)
		elif remove=='n':
			print("That's nice! I wouldn't like you to go") 
	else:
		print('I dont think I know you {}'.format(name))
		add_user= input('Would you like to be added to the system (y/n)?: ').strip().lower()
		if add_user=='y':
			known_users.append(name)
		elif add_user=='n':
			print('No worries, see you later!')



 

