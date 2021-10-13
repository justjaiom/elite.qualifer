# ELite Qualifier progect is bases on a chatbox  it is a yo mama showdowm=n, the code will repsond baded on what kind of roast you type
import random 
import sys
from time import sleep
random_number = random.randint(1, 5)
random_stupid_roast = random.randint(1, 5)
random_fat_roast = random.randint(1, 5)
random_ugly_roast = random.randint(1, 5)
random_old_roast = random.randint(1, 5)



print("welcome to yo mama showdown")

print("your roast should either have the words fat, stupid,ugly,or old") ; sleep(.75)
print("starting in 3")
print('2') ; sleep(.75)
print('1') ; sleep(.75)
  
print("roast!")


term = "fat" #term we want to search for
term2 = "stupid"
term3 = "ugly"
term4 = "old"
input = input() #read input from user

words = input.split() #split the sentence into individual words

if term in words: #see if one of the words in the sentence is the word we want
  if random_fat_roast == 1:
    print("Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up")
  if random_fat_roast == 2:
    print("Yo mama's so fat, when she skips a meal, the stock market drops.")
  if random_fat_roast == 3:
    print("Yo mama's so fat, she stepped on a scale and it said: To be continued")
  if random_fat_roast == 4:
    print("Yo mama's so fat, when she wears high heels, she strikes oil")
  if random_fat_roast == 5:
    print("Yo mama's so fat, she can't even jump to a conclusion")

if term2 in words:

  if random_stupid_roast == 1:
   print("Yo mama's so stupid, she stared at a cup of orange juice for 12 hours because it said concentrate")
  if random_stupid_roast == 2:
     print("Yo mama's so stupid when they said it was chilly outside, she grabbed a bowl")
  if random_stupid_roast == 3:
      print("Yo mama's so stupid, when they said, Order in the court,she asked for fries and a shake.")
  if random_stupid_roast == 4:
      print("Yo mama's so stupid, she got hit by a parked car")
  if random_stupid_roast == 5:
      print("Yo mama's so stupid, when I told her that she lost her mind, she went looking for it")
if term3 in words:
  if random_ugly_roast == 1:
    print("Yo mama's so ugly, she threw a boomerang and it refused to come back")
  if random_ugly_roast == 2:
    print("Yo mama's so ugly, she made a blind kid cry")
  if random_ugly_roast == 3:
    print("Yo mama's so ugly, her portraits hang themselves")
  if random_ugly_roast == 4:
    print("Yo mama's so ugly, her birth certificate is an apology letter")
  if random_ugly_roast == 5:
    print("yo mama so ugly gold fish stoped smiling back")

if term4 in words:
  if random_old_roast ==1:
    print("Yo mama's so old, her social security number is one")
  if random_old_roast ==2:
    print("Yo mama's so old, she walked out of a museum and the alarm went off")
  if random_old_roast ==3:
    print("yo mama so old when she was in school there was no history class")
  if random_old_roast ==4:
    print("yo mama so old she fats dust")
  if random_old_roast ==5:
    print("yo mama so old she has a signed bible")
print("---------------------------------")
print("bonus round")
print('3') ; sleep(0.5)
print('2') ; sleep(0.5)
print('1') ; sleep(0.5)


