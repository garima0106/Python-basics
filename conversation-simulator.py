from random import choice
questions =["Why is it a holiday?", "Why is it so hot?", "Why are you mad at me?"]
question=choice(questions)
answer=input(question).strip().lower()
while answer!='just because':
	answer=input("why?: ").strip().lower()
print("Oh ok..")
	


