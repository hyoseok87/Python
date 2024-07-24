#day10 - 1
def formant_name(f_name, l_name):
    formatd_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formatd_f_name} {formated_l_name}"

formated_string = formant_name("vinCent","ecKardt")
print(formated_string)

#day10 - 2
def formant_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs."
    formatd_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formatd_f_name} {formated_l_name}"

#day10 - 3
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")


# TODO: Add more code here 👇
def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)



