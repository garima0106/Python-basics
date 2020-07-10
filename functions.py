def rev(s):
	#text=input("Enter the word to be reversed: ").strip().lower()
	return print(s[::-1])

text=input("Enter the word to be reversed: ").strip().lower()
rev(text) 

a=100
b=[1,3,4]
def f1():
	global a
	a=200 
	print(a)
	b[0]=8
	b[1]=12
	b[2]=16
	print(b)

def f2():
	print(a)

f1()
f2()
print(a)
print(b)

#pack/unpack positional args
def addme(*numbers):
	total=0
	for n in numbers:
		total=total+n
	return total


num=[1,2,4,56,7]
sum=addme(*num)
print(sum)


def about(name="Garima",age=40,likes="Badminton"):
	sentence="My name is {}, I am {} years old and I like to play {}".format(name, age, likes)
	return print(sentence)


about()
name=input("Enter your name: ").strip().capitalize()
dictionary={"name":name,"age":23,"likes":"Football"}
about(**dictionary)
dict2={"likes":"basketball","name":"George","age":32}
about(**dict2)


#pack/unpack key args
def foo(**kargs):
	for key, value in kargs.items():
		print("{}:{}".format(key, value))


foo(red="color",square="size")

