import os

def clear():
    os.system("cls")

def get_float(msg, fail = "Invalid."):
    try:
        ans = float(input(msg))
    except Exception as e:
        print(fail)
        return get_float(msg, fail)
    return ans

def get_bmi():
    weight = get_float("Enter weight in pounds: ")
    height = get_float("Enter height in inches: ")

    bmi = 703 * weight / (height**2)

    print("BMI is " + str(bmi))

    return bmi

def get_classif(bmi):
    print()
    if bmi < 18.5:
        print("Classification: Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Classification: Normal")
    elif bmi >= 25 and bmi < 30:
        print("Classification: Overweight")
    elif bmi >= 30:
        print("Classification: Obese")
    else:
        print("ERROR")


bmi = get_bmi()
get_classif(bmi)