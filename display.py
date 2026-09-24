def display_profile(name, age, height, weight, bmi, category):

    print("\n================================")
    print("       HEALTH PROFILE")
    print("================================")

    print("Name:", name)
    print("Age:", age)
    print("Height:", height, "m")
    print("Weight:", weight, "kg")
    print("BMI:", round(bmi, 2))
    print("BMI Category:", category)


def display_averages(averages):

    average_water, average_sleep, average_steps, average_exercise = averages

    print("\n================================")
    print("       HEALTH SUMMARY")
    print("================================")

    print("Average Water Intake:",
          round(average_water, 2), "litres")

    print("Average Sleep:",
          round(average_sleep, 2), "hours")

    print("Average Steps:",
          round(average_steps, 2))

    print("Average Exercise:",
          round(average_exercise, 2), "minutes")


def display_final_report(records, bmi, category):

    print("\n========================================")
    print("          FINAL HEALTH REPORT")
    print("========================================")

    print("Total Days Tracked:", len(records))
    print("BMI:", round(bmi, 2))
    print("BMI Category:", category)

    print("\nDaily Records:")

    for record in records:

        print("--------------------------------")
        print("Date:", record["date"])
        print("Water:", record["water"], "litres")
        print("Sleep:", record["sleep"], "hours")
        print("Steps:", record["steps"])
        print("Exercise:", record["exercise"], "minutes")

    print("\n========================================")
    
def display_all_records(records):

    print("\n================================")
    print("       ALL HEALTH RECORDS")
    print("================================")

    for record in records:

        print("\n----------------------------")
        print("Date:", record["date"])
        print("Water:", record["water"], "litres")
        print("Sleep:", record["sleep"], "hours")
        print("Steps:", record["steps"])
        print("Exercise:", record["exercise"], "minutes")