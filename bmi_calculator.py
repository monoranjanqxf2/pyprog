"""
BMI calculator
SCOPE:
1.Read user's height
2.Read user's weight
3.Calculate BMI
4.Print BMI 
"""
user_height=float(input("Enter height as meter : "))
user_weight=int(input("Enetr weight as KG : "))
BMI=user_weight/user_height**2
print(f"Your BMI is {BMI}")