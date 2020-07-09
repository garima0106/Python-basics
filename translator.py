vowels=0
consonants=0
for letter in "Hello World":
	if letter.lower() in "aeiou":
		vowels=vowels+1
	elif letter.lower() in "":
		pass
	else:
		consonants=consonants+1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

students={"male":["Tom","Charlie","John","Gorgy","Sam"], "female":["Sarah","Kia","Myra","Niki"]}

for keys in students.keys():
	for name in students[keys]:
		if 'a' in name:
			print(name)

# lets play Pig Latin
print("Let's play Pig Latin!")
#get sentence from user 
sentence= input("Give me a sentence! ").strip().lower()

# split the sentence into words

words=sentence.split()
print(words)


#loop through each word and translate it to pig latin form

new_words=[]

#pig translation rules
# if the word starts fron vowel, add 'yay'
# if it starts from consonant, move the consonant cluster to the end and add 'ay'
for word in words:
	
	if word[0] in "aieou":
		new_word = word + 'yay'
		new_words.append(new_word)
	else:
		vowel_pos=0;
		for letter in word:
			if letter not in "aieou":
			 	vowel_pos=vowel_pos+1
			else:
				break
		
		cons=word[:vowel_pos]
		the_rest=word[vowel_pos:]
		new_word=the_rest+cons+'ay'
		new_words.append(new_word)


#put all the words back to sentence

output= " ".join(new_words)
#print the translated sentence
print(output)











