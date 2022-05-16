# Collect User input
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

# BMI calculation
bmi = round(weight / height ** 2, 2)