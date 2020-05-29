# monobank stakes
monobank_3m_perc_month = 9.66
monobank_3m_perc_reinvest = 9.74
monobank_6m_perc_month = 10.06
monobank_6m_perc_reinvest = 10.27
monobank_12m_perc_month = 10.47
monobank_12m_perc_reinvest = 11.43

# deposit terms
term_3month = 3
term_6month = 6
term_12month = 12

# user data
user_name = input("What's your name? ")
deposit_term = int(input("What's the term of deposit? 3, 6 or 12 months "))
deposit_sum = int(input("What's the sum you want to deposit? "))

# Formulas
income_3month = deposit_sum / 100 * monobank_3m_perc_month / 12 * deposit_term
income_6month = deposit_sum / 100 * monobank_6m_perc_month / 12 * deposit_term
income_12month = deposit_sum / 100 * monobank_12m_perc_month


# Options
option_selection = int(input("Enter 1 if you want to calculate with monobank stakes or Enter 2 if you want to enter your stakes "))
if option_selection == 1:
    print(deposit_sum)
    print(deposit_term)
    if deposit_term == 3:
        print('Your income will be ',income_3month)
    elif deposit_term == 6:
        print('Your income will be ',income_6month)
    elif deposit_term == 12:
        print('Your income will be ',income_12month)
elif option_selection == 2:
    user_percents = float(input("What's the stake? "))
    income_user = deposit_sum / 100 * user_percents / 12 * deposit_term
    print('Your income will be ',income_user)
