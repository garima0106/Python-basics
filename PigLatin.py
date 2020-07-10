# ask user any sentence

sentence=input("Enter any sentence: ").strip().lower()

#split that sentence into words

words= sentence.split()
#print(words)

# we need to create a bag of new words

new_words=[]

#for each word check the first letter 
for word in words:
		if word[0] in 'aieou':
			new_word= word+'yay'
			new_words.append(new_word)
		
		else:
			vowel_at=0
			for letter in word:
				if letter not in 'aieou':
					vowel_at=vowel_at+1
				else:
					break
			cons=word[:vowel_at]
			new_word=word[vowel_at:]+cons+'ay'
			new_words.append(new_word)


#if it is a vowel then add 'yay' to the word and add to the bag of new words

#if it is a consonant then pick all the consonants and add them to the end of the word and add 'ay' to the end of the word, add this word to the bag of new words

#add all the words to a sentence

#print the sentence
output=" ".join(new_words)
print(output)
