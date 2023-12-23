#if/else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you are not tall enough to ride the rollercoaster")
# = : Assignment = 하나일 때는 변수 값을 대입하는 것
# == : Comparing = 두개일 때는 왼쪽에 있는 값이 오른쪽에 있는 값과 같은지 확인

#이중 조건문(Nested if/else)
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age <= 18:
#     print("Please pay $7")
#   else:
#     print("Please pay $12")
# else:
#   print("Sorry, you are not tall enough to ride the rollercoaster")

#if/elif/else
#

#다중 if문(Multiple if)
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height > 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5")
#   elif age <= 18:
#       bill = 7
#       print("Youth tickets are $7")
#   else:
#     bill = 12
#     print("Adult tickets are $12")

#   wants_photo = input("Do you want a photo taken? (Y/N)").upper()
#   if wants_photo == "Y":
#     bill += 3

#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you are not tall enough to ride the rollercoaster")

#Logical Operatiors
# and : &&
# or : ||
# not : !
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height > 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us")
#   else:
#     bill = 12
#     print("Adult tickets are $12")

#   wants_photo = input("Do you want a photo taken? (Y/N)").upper()
#   if wants_photo == "Y":
#     bill += 3

#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you are not tall enough to ride the rollercoaster")
#Love caculator
#My Code
# name1 = input("What is your name?")
# name2 = input("What is your name?")

# name1 = name1.lower()
# name2 = name2.lower()

# total_t = name1.count("t") + name2.count("t")
# total_r = name1.count("r") + name2.count("r")
# total_u = name1.count("u") + name2.count("u")
# total_e = name1.count("e") + name2.count("e")
# total = total_t + total_r + total_u + total_e

# total_l = name1.count("l") + name2.count("l")
# total_o = name1.count("o") + name2.count("o")
# total_v = name1.count("v") + name2.count("v")
# total_e = name1.count("e") + name2.count("e")
# total_love = total_l + total_o + total_v + total_e

# love_score = int(str(total) + str(total_love))

# if love_score <10 or love_score >90:
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif  40 <= love_score <=50:
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")

#Angela Code
# print("The Love Calculator is calculating your score...")
# name1 = input("What is your name?")
# name2 = input("What is their name?")

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

#Day3_Project Tresure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "yellow":
      print("You found the treasure!")
    else:
      print("You got eaten by a Orger.Game Over")
  else:
    print("A shark has bitten you.Game Over")
else:
  print("Dragon killed you. Game Over")
