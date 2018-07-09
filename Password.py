import re
#string validation for alphabetic characters
def name():
  while True:
    fname=input('What is your name? ')
    if re.match(r'^([a-zA-Z\s]*$)', fname):
      print (fname)
      break
    else:
      print('Try again, only alphabetical characters: ')

#string validation for alphabetic characters
def passwordId():
  while True:
    password=input('Enter a password that consisits of: 8 characters, lower and uppercase letters, a number, and a special character. ')
    if re.match(r'^(?=\S{8,}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])', password):
      print (password)
      break
    else:
      print('ERROR, password must include: 8 characters , a number, special characters, lower and uppercase letters.')

name()
passwordId()


#variable for yes input
yess=['yes','Yes', 'YES', 'y', "Y"]

#asks users if they would like to try caesar cyper again
def tryagain():
  again = input("Would you like to try again? Please type yes or any alphanumeric character for no: ")
  if again in yess:
    loopBack()
  else:
    print ("Thank you, goodbye!")
    exit()

#loops all variables if they choose to do so again
def loopBack():
  fname = name()
  password = passwordId()
  again = tryagain()

tryagain()
loopBack()

wasssss goooooooood
