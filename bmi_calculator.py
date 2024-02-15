#User Input
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

#BMI Calculation
bmi = weight / (height ** 2)

#Health Category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

#Command Line Interface
print(f"Your BMI is {bmi:.2f}, and you are in the '{category}' category.")
