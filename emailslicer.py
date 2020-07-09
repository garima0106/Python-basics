# get user email address
email= input("Enter your email address: ").strip()

#slice out user name

username= email[0:email.index('@')]

#slice out domain name
#garimagr@gmail.com
ind=email.index('@')+1
domainname= email[ind:]

#format message

message= "The user name is {} and the domain name is {}"
output=message.format(username,domainname)

#print on screen
print(output)

