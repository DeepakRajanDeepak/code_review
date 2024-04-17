import json
import os

def prompt(message):
    if message == "result":
        print(f"==> {data[lang][message]} ${round(monthly_payment, 2)}")
    else:
        print(f"==> {data[lang][message]}")

def compute_lang_not_valid(code):
    return code not in ['en', 'de', 'fr']

def compute_not_valid(number_string):
    try:
        number = float(number_string)
        if number_string.strip().lower() == "nan":
            raise ValueError(f"Value cannot be {number_string}")
        if number < 0:
            raise ValueError("Value cannot be less than 0")
    except TypeError:
        return True
    except ValueError:
        return True
    return False

def compute_not_integer(number_string):
    number = float(number_string)
    return int(number) != number

with open('mortgage.json', 'r') as file:
    data = json.load(file)

lang = "lang"
prompt("welcome")
prompt("english")
prompt("german")
prompt("french")
lang = input()

while compute_lang_not_valid(lang):
    lang = "lang"
    prompt("bad_lang")
    lang = input()

while True:
    os.system('clear')
    prompt("welcome")
    prompt("separator")
    prompt("loan")
    loan_amount = input()

    while compute_not_valid(loan_amount):
        prompt("bad_loan")
        loan_amount = input()

    prompt("apr")
    annual_rate = input()

    while compute_not_valid(annual_rate):
        prompt("bad_apr")
        annual_rate = input()

    prompt("years")
    loan_years = input()

    while compute_not_valid(loan_years) or compute_not_integer(loan_years):
        prompt("bad_years")
        loan_years = input()

    prompt("months")
    loan_months = input()

    while compute_not_valid(loan_months) or compute_not_integer(loan_months):
        prompt("bad_months")
        loan_months = input()

    loan_amount = float(loan_amount)
    annual_rate = float(annual_rate)
    loan_years = float(loan_years)
    loan_months = float(loan_months)

    monthly_rate = (annual_rate / 12) / 100
    months = loan_years * 12 + loan_months

    monthly_payment = loan_amount * (
        monthly_rate
                / (1 - (1 + monthly_rate) ** (-months)))

    prompt("result")
    prompt("continue")
    answer = input().lower()

    while not(answer.startswith('n') or answer.startswith('y')):
        prompt("bad_continue")
        answer = input().lower()

    if answer[0] == 'n':
        break

os.system('clear')
prompt("farewell")
