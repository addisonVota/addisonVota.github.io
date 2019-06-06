import random
Question = raw_input("Please choose either odd or even: ")
if Question == "odd" or Question == "even" :
  Question_number=int(input("Pick a number between 0 and 5"))
else:
  raw_input("Please choose either odd or even: ")
bool_number = False
if Question >= 0 or Question <= 5:
  bool_number = True

else:
  print("Please type in odd or even next time.")
  quit()
  
bot_number = random.randint(0,5)

if bool_number == True:
  print("My number is %s.") % bot_number
else:
  quit()
  
Answer = Question_number + bot_number
print "Your number was %s. My number was %s. The sum these is %s." % (Question_number,bot_number,Answer)
if (Answer % 2) == 0 and "even" in Question:
  print "The sum is even. You win!"
elif (Answer % 2) == 0 and "odd" in Question:
  print "The sum is even. You lose."
elif (Answer % 2) == 1 and "odd" in Question:
  print "The sum is odd. You win!"
elif (Answer % 2) == 1 and "even" in Question:
  print "The sum is odd. You lose."
