print("Welcome to simple interest calculator.")
print(" ")

principle = float(input("Enter the principle amount: "))
print("Principle = ", principle)
print(" ")

rate = float(input("Enter the rate of interest: "))
print("Rate of Interest = ", rate)
print(" ")

time = float(input("Enter the time(in years) for which the amount is taken: "))
print("Time period = ", time)
print(" ")

numerator = float(principle*rate*time)
simple_interest = numerator/100
amount = simple_interest+principle

print("Formula for simple interest = Principle x Rate of Interest x Time / 100")
print("Simple Interest = ", simple_interest)

print(" ")

print("Formula for calculating total amount = Simple Interest + Principle")
print("Total amount after", time, "years at", rate, "%", "rate of interest for the amount", principle, "will be = ", amount)

print(" ")