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
bmi=user_weight/user_height**2
print(f"Your BMI is {bmi}")
if(bmi<16):
    print("You are underweighted")
elif(bmi>=16 and bmi<22):
    print("You are normal")
elif(bmi>=22 and bmi<28):
    print("You are overweighted")
else:
    print("You are ")