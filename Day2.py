##Data Types
#String:Hello
#print("Hello"[0])
#print("Hello"[4])

#"12345" it is also a string.

#print("123" + "345")
#print(123+345)

#Integer:1,2,3,4 소수점이 없는 숫자를 의미
#print(123 + 678)

#Float: 소수점이 있는 숫자를 의미
#3.14159

#Boolean: True, False

# num_char =len(input("What is your name?"))


# print("Your name has", num_char, "characters")")
#print(type(num_char))

#Type을 통해 데이터 형식이 확인 가능
# new_num_char = str(num_char)
# print("Your name has " +  new_num_char + " characters.")
#str 등을 통해 모든 데이터를 변환이 가능하다 문자->숫자 등등

# a = str(123)
# print(type(a))

# b = float(123)

# print(70 + flot("100.5"))
# print(str(70) + str(100))

#PEMDASLR
# print(2**3): 제곱

#print(3 * 3 + 3 / 3 - 3):7
#Instead of 7 make the Result 3
#print(3 * (3 + 3) / 3 - 3)

# print("BMI " + " Caulculator")
# height = input("What is your height?")
# weight = input("What is your weight?")
# height1 = float(height)
# weight1 = float(weight)
# bmi = weight1 / (height1 ** 2)
# bmi1 = float(bmi) * 10000
# print(int(bmi1))

#F-String
# score = 0
# height = 1.8
# isWinning = True

# print(f"Your score is {score}, your height is {height}, and you are winning? {isWinning}")
# #Übung1: Life in Weeks
# age = input("What is your age?")
# years = 90 - int(age)
# weeks = years * 52
# print(f"You have {weeks} weeks left.")

#Project2: Tip Calculator
print("Welcome to the tip calculator")
price= input("What is your total bill?")
tip = input("What percentage tip would you like to give? 10, 12 or 15?")
split_bill = input("How many people to split the bill?")
each_person_pays = round(float(price) * (1 + float(tip) / 100) / int(split_bill), 2)
print(f"Each person should pay ${each_person_pays}")