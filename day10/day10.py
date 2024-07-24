# #day10 - 1
# def formant_name(f_name, l_name):
#     formatd_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formatd_f_name} {formated_l_name}"
#
# formated_string = formant_name("vinCent","ecKardt")
# print(formated_string)
#
# #day10 - 2
# def formant_name(f_name, l_name):
#
#     if f_name == "" or l_name == "":
#         return "You didnt provide valid inputs."
#     formatd_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formatd_f_name} {formated_l_name}"

#day10 - 3
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    elif month > 12 or month < 1 :
        return "Geben Sie nur von 1 bis 12 Monat ein."
    else:
        return month_days[month - 1]


def main():
    continue_program = True
    while continue_program:
        year = int(input("Geben Sie Year ein: "))  # Enter a year

        while True:
            month = int(input("Geben Sie Monat ein: "))  # Enter a month
            days = days_in_month(year, month)
            if isinstance(days, int):
                break
            else:
                print(days)
                # Prompt the user to enter year again if the month input is invalid


        print(days)

        retry = input("Möchten Sie erneut eingeben? (y/n): ").strip().lower()
        if retry != 'y':
            continue_program = False

if __name__ == "__main__":
    main()






