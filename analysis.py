def calculate_averages(records):

    total_water = 0
    total_sleep = 0
    total_steps = 0
    total_exercise = 0

    for record in records:
        total_water = total_water + record["water"]
        total_sleep = total_sleep + record["sleep"]
        total_steps = total_steps + record["steps"]
        total_exercise = total_exercise + record["exercise"]

    number_of_records = len(records)

    average_water = total_water / number_of_records
    average_sleep = total_sleep / number_of_records
    average_steps = total_steps / number_of_records
    average_exercise = total_exercise / number_of_records

    return average_water, average_sleep, average_steps, average_exercise


def analyse_record(record):

    print("\n--- Health Analysis ---")

    if record["water"] >= 2:
        print("Water Intake: Good")
    else:
        print("Water Intake: Low")

    if record["sleep"] >= 7:
        print("Sleep: Good")
    else:
        print("Sleep: Low")

    if record["steps"] >= 5000:
        print("Steps: Good")
    else:
        print("Steps: Low")

    if record["exercise"] >= 30:
        print("Exercise: Good")
    else:
        print("Exercise: Low")


def find_highest_steps(records):

    highest = records[0]

    for record in records:
        if record["steps"] > highest["steps"]:
            highest = record

    return highest


def find_lowest_steps(records):

    lowest = records[0]

    for record in records:
        if record["steps"] < lowest["steps"]:
            lowest = record

    return lowest
def calculate_health_score(record):

    score = 0

    if record["water"] >= 2:
        score = score + 1

    if record["sleep"] >= 7:
        score = score + 1

    if record["steps"] >= 5000:
        score = score + 1

    if record["exercise"] >= 30:
        score = score + 1

    return score