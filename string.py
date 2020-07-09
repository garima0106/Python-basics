str= 'hello world!'
print(str)
para='''My name is Garima, how are you doing today
I am in Tempe
how is the weather
Lets learn python from scratch'''
print(para)

#Ask user's name
name= input("Enter your name: ")

# Ask user's age
age= input("What's your age?: ")

# ask user's city
city= input("Which city you live in?: ")
# ask about user's interest
love=input("What are you interest?: ")
print("="*20)
print('The info we have about you:')
print('='*20)
string = "Your name is {}, you are {} years old, you live in {} and you love to {}"
# format the output
output= string.format(name,age,city, love)
#print to the screen
print(output) 

