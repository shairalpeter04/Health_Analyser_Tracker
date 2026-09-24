def get_profile():

    name = input("Enter your name: ")

    # Validate age
    while True:
        try:
            age = int(input("Enter your age: "))

            if age > 0:
                break
            else:
                print("Age must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Validate height
    while True:
        try:
            height = float(input("Enter your height in metres: "))

            if height > 0:
                break
            else:
                print("Height must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Validate weight
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))

            if weight > 0:
                break
            else:
                print("Weight must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    return name, age, height, weight


def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obesity"