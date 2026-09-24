from profile import get_profile, calculate_bmi, bmi_category
from tracker import add_daily_record, display_record

from analysis import (
    calculate_averages,
    analyse_record,
    find_highest_steps,
    find_lowest_steps,
    calculate_health_score
)
from display import (
    display_profile,
    display_averages,
    display_final_report,
    display_all_records
)


print("========================================")
print("       HEALTH ANALYSER & TRACKER")
print("========================================")


# Get user profile
name, age, height, weight = get_profile()


# Calculate BMI
bmi = calculate_bmi(height, weight)
category = bmi_category(bmi)


# Display profile
display_profile(name, age, height, weight, bmi, category)


# Store daily records
records = []


# Main Menu
while True:

    print("\n================================")
    print("           MAIN MENU")
    print("================================")
    print("1. Add Daily Health Record")
    print("2. View Current Record")
    print("3. View Health Analysis")
    print("4. Finish Tracking")

    choice = input("Enter your choice: ")


    # Option 1
    if choice == "1":

        record = add_daily_record()

        records.append(record)

        print("\nRecord added successfully!")


    # Option 2
    elif choice == "2":

        if len(records) == 0:

           print("\nNo records available.")

        else:

           display_all_records(records)


    # Option 3
    elif choice == "3":

        if len(records) == 0:

            print("\nNo records available for analysis.")

        else:

            averages = calculate_averages(records)

            display_averages(averages)


            highest = find_highest_steps(records)

            lowest = find_lowest_steps(records)


            print("\n--- Step Summary ---")

            print("Highest Steps:", highest["steps"])

            print("Lowest Steps:", lowest["steps"])


            analyse_record(records[-1])


            # Health Score
            score = calculate_health_score(records[-1])

            print("\nHealth Score:", score, "/ 4")


    # Option 4
    elif choice == "4":

        break


    # Invalid choice
    else:

        print("\nInvalid choice. Please enter 1, 2, 3 or 4.")


# Final Report
if len(records) > 0:

    averages = calculate_averages(records)

    display_final_report(records, bmi, category)


    highest = find_highest_steps(records)

    lowest = find_lowest_steps(records)


    print("\n--- Final Step Summary ---")

    print("Highest Steps:", highest["steps"])

    print("Lowest Steps:", lowest["steps"])


else:

    print("\nNo daily records were added.")


print("\n========================================")
print("       THANK YOU FOR USING THE APP")
print("========================================")