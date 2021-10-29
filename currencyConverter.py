print("Choose the currency code you want to convert FROM: ")
print(" ")
print("Type 1 for INR - Indian Rupee.")
print("Type 2 for USD - United States Dollar.")
print("Type 3 for EUR - Euro.")
print("Type 4 for AUD - Australian Dollar.")
print("Type 5 for CAD - Canadian Dollar.")
print("Type 6 for GBP - British Pound.")

print(" ")
from_currency = int(input("Enter your number:- "))
print(" ")

x = float(input("Enter the amount that you want to convert: "))
print(" ")


print("Choose the currency code you want to convert the amount TO: ")
print(" ")
print("Type 1 for INR - Indian Rupee.")
print("Type 2 for USD - United States Dollar.")
print("Type 3 for EUR - Euro.")
print("Type 4 for AUD - Australian Dollar.")
print("Type 5 for CAD - Canadian Dollar.")
print("Type 6 for GBP - British Pound.")

print(" ")
to_currency = int(input("Enter your number:- "))
print(" ")


if from_currency == 1:
    if to_currency == 1:
        inr = float(x*1)
        print("Indian Rupee(INR)", x, "in Indian Rupee(INR) will amount to", inr)

    if to_currency == 2:
        usd = float(x*0.013)
        print("Indian Rupee(INR)", x, "in United States Dollar(USD) will amount to", usd)

    if to_currency == 3:
        eur = float(x*0.011)
        print("Indian Rupee(INR)", x, "in Euro(EUR) will amount to", eur)

    if to_currency == 4:
        aud = float(x*0.017)
        print("Indian Rupee(INR)", x, "in Australian Dollar(AUD) will amount to", aud)

    if to_currency == 5:
        cad = float(x*0.017)
        print("Indian Rupee(INR)", x, "in Canadian Dollar(CAD) will amount to", cad)

    if to_currency == 6:
        gbp = float(x*0.0095)
        print("Indian Rupee(INR)", x, "in British Pound(GBP) will amount to", gbp)

    if to_currency>=7:
        print("Enter either 1,2,3,4,5 or 6.")




if from_currency == 2:
    if to_currency == 1:
        inr = float(x*74.90)
        print("United States Dollar(USD)", x, "in Indian Rupee(INR) will amount to", inr)

    if to_currency == 2:
        usd = float(x*1)
        print("United States Dollar(USD)", x, "in United States Dollar(USD) will amount to", usd)

    if to_currency == 3:
        eur = float(x*0.83)
        print("United States Dollar(USD)", x, "in Euro(EUR) will amount to", eur)

    if to_currency == 4:
        aud = float(x*1.29)
        print("United States Dollar(USD)", x, "in Australian Dollar(AUD) will amount to", aud)

    if to_currency == 5:
        cad = float(x*1.25)
        print("United States Dollar(USD)", x, "in Canadian Dollar(CAD) will amount to", cad)

    if to_currency == 6:
        gbp = float(x*0.71)
        print("United States Dollar(USD)", x, "in British Pound(GBP) will amount to", gbp)

    if to_currency>=7:
        print("Enter either 1,2,3,4,5 or 6.")




if from_currency == 3:
    if to_currency == 1:
        inr = float(x*90.15)
        print("Euro(EUR)", x, "in Indian Rupee(INR) will amount to", inr)

    if to_currency == 2:
        usd = float(x*1.20)
        print("Euro(EUR)", x, "in United States Dollar(USD) will amount to", usd)

    if to_currency == 3:
        eur = float(x*1)
        print("Euro(EUR)", x, "in Euro(EUR) will amount to", eur)

    if to_currency == 4:
        aud = float(x*1.55)
        print("Euro(EUR)", x, "in Australian Dollar(AUD) will amount to", aud)

    if to_currency == 5:
        cad = float(x*1.51)
        print("Euro(EUR)", x, "in Canadian Dollar(CAD) will amount to", cad)

    if to_currency == 6:
        gbp = float(x*0.86)
        print("Euro(EUR)", x, "in British Pound(GBP) will amount to", gbp)

    if to_currency>=7:
        print("Enter either 1,2,3,4,5 or 6.")




if from_currency == 4:
    if to_currency == 1:
        inr = float(x*58.06)
        print("Australian Dollar(AUD)", x, "in Indian Rupee(INR) will amount to", inr)

    if to_currency == 2:
        usd = float(x*0.78)
        print("Australian Dollar(AUD)", x, "in United States Dollar(USD) will amount to", usd)

    if to_currency == 3:
        eur = float(x*0.64)
        print("Australian Dollar(AUD)", x, "in Euro(EUR) will amount to", eur)

    if to_currency == 4:
        aud = float(x*1)
        print("Australian Dollar(AUD)", x, "in Australian Dollar(AUD) will amount to", aud)

    if to_currency == 5:
        cad = float(x*0.97)
        print("Australian Dollar(AUD)", x, "in Canadian Dollar(CAD) will amount to", cad)

    if to_currency == 6:
        gbp = float(x*0.55)
        print("Australian Dollar(AUD)", x, "in British Pound(GBP) will amount to", gbp)

    if to_currency>=7:
        print("Enter either 1,2,3,4,5 or 6.")





if from_currency == 5:
    if to_currency == 1:
        inr = float(x*59.73)
        print("Canadian Dollar(CAD)", x, "in Indian Rupee(INR) will amount to", inr)

    if to_currency == 2:
        usd = float(x*0.80)
        print("Canadian Dollar(CAD)", x, "in United States Dollar(USD) will amount to", usd)

    if to_currency == 3:
        eur = float(x*0.66)
        print("Canadian Dollar(CAD)", x, "in Euro(EUR) will amount to", eur)

    if to_currency == 4:
        aud = float(x*1.03)
        print("Canadian Dollar(CAD)", x, "in Australian Dollar(AUD) will amount to", aud)

    if to_currency == 5:
        cad = float(x*1)
        print("Canadian Dollar(CAD)", x, "in Canadian Dollar(CAD) will amount to", cad)

    if to_currency == 6:
        gbp = float(x*0.57)
        print("Canadian Dollar(CAD)", x, "in British Pound(GBP) will amount to", gbp)

    if to_currency>=7:
        print("Enter either 1,2,3,4,5 or 6.")





if from_currency == 6:
    if to_currency == 1:
        inr = float(x*104.75)
        print("British Pound(GBP)", x, "in Indian Rupee(INR) will amount to", inr)

    if to_currency == 2:
        usd = float(x*1.40)
        print("British Pound(GBP)", x, "in United States Dollar(USD) will amount to", usd)

    if to_currency == 3:
        eur = float(x*1.16)
        print("British Pound(GBP)", x, "in Euro(EUR) will amount to", eur)

    if to_currency == 4:
        aud = float(x*1.80)
        print("British Pound(GBP)", x, "in Australian Dollar(AUD) will amount to", aud)

    if to_currency == 5:
        cad = float(x*1.75)
        print("British Pound(GBP)", x, "in Canadian Dollar(CAD) will amount to", cad)

    if to_currency == 6:
        gbp = float(x*1)
        print("British Pound(GBP)", x, "in British Pound(GBP) will amount to", gbp)

    if to_currency>=7:
        print("Enter either 1,2,3,4,5 or 6.")




if from_currency>=7:
            print("Enter either 1,2,3,4,5 or 6.")