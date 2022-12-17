print('Welcome to the tip calculator')
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give?"))
number_of_people = int(input("How many people should split the bill?"))
total_factor = (tip_percentage/100) + 1
total_amount = (bill*total_factor)
each_pay = round(total_amount/number_of_people,2)

print(f"Each person should pay: ${each_pay}")

