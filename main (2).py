#input1 is the variable and "input" means that the string is a question and requires an answer 
input1 =  input("Welcome to your virtual Python Caclulator What system do you require today : 1- addition 2- subtraction 3- multiplication 4- division  ")
# the if statements see what input you enters and continues accordingly
if input1 == "1":
  num1 = input("what is your first number?  ")
  num2 = input("what is your second number?  ")
  print (str(num1) , "+" , str(num2) , "=" ,  int(num1)+int(num2))
  # the print value requires int in front of the variable because otherwise it will simply write them next to each other with no space instead of treating them as number values and addind them together
if input1 == "2":
  num1 = input("what is your first number?  ")
  num2 = input("what is your second number?  ")
  print (str(num1) , "-" , str(num2) , "=" ,  int(num1)-int(num2))
if input1 == "3":
  num1 = input("what is your first number?  ")
  num2 = input("what is your second number?  ")
  print (str(num1) , "x" , str(num2) , "=" ,  int(num1)*int(num2))
if input1 == "4":
  num1 = input("what is your first number?  ")
  num2 = input("what is your second number?  ")
  print (str(num1) , "/" , str(num2) , "=" ,  int(num1)/int(num2))
