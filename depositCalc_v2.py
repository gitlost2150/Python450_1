 # user data
percent = 0

user_name = input("What's your name? ")

deposit_term = int(input("What's the term of deposit, " + user_name + "?" " 3, 6 or 12 months ?  "))
if deposit_term > 0 and deposit_term < 6:
    percent = 9
    print("Your rate percent is ", percent)
elif deposit_term >= 6 and deposit_term < 12:
    percent = 10  
    print("Your rate percent is ", percent)  
elif deposit_term >= 12:
    percent = 11
    print("Your rate percent is ", percent)
else:
    print("Not valid value! Please try again")

deposit_sum = int(input("What's the sum you want to deposit? "))

class depositPercents:
    def __init__(self, percent, date):
        self.percent = percent
        self.date = date


monthPercent = depositPercents(percent ,deposit_term)

# Formulas
incomeGeneral = deposit_sum / 100 * monthPercent.percent / 12 * monthPercent.date

#Result
print("****************************************")
print("Your income is ", incomeGeneral , " UAH")
print("****************************************")