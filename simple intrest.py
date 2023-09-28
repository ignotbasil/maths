principal= float(input("ENTER THE PRINCIPAL  AMOUNT: "))
rate= float(input("ENTER THE RATE OF INTREST (IN PERCENTAGE): "))
time= float(input("ENTER THE TIME PERIOD (in years): "))

simple_interest = (principal * rate * (time/12)/ 100)

print("Simple Interest:", simple_interest)
