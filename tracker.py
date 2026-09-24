def add_daily_record():

    print("\n--- Daily Health Record ---")

    date = input("Enter date (DD-MM-YYYY): ")

    # Validate water intake
    while True:
        try:
            water = float(input("Enter water intake (litres): "))

            if water >= 0:
                break
            else:
                print("Water intake cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")

    # Validate sleep
    while True:
        try:
            sleep = float(input("Enter sleep hours: "))

            if sleep >= 0:
                break
            else:
                print("Sleep hours cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")

    # Validate steps
    while True:
        try:
            steps = int(input("Enter number of steps: "))

            if steps >= 0:
                break
            else:
                print("Steps cannot be negative.")

        except ValueError:
            print("Please enter a whole number.")

    # Validate exercise
    while True:
        try:
            exercise = float(input("Enter exercise duration (minutes): "))

            if exercise >= 0:
                break
            else:
                print("Exercise duration cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")

    record = {
    "date": date,
    "water": water,
    "sleep": sleep,
    "steps": steps,
    "exercise": exercise
}

    return record


def display_record(record):
    print("\n--- Today's Record ---")

    print("Water Intake:", record["water"], "litres")
    print("Sleep:", record["sleep"], "hours")
    print("Steps:", record["steps"])
    print("Exercise:", record["exercise"], "minutes")