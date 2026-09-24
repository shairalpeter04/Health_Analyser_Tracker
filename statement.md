# Health Analyser & Tracker

## 1. Problem Statement

It is helpful for users to keep record of their daily habits such as their water intake, sleep, exercise and the number of steps they take since this enables them to become aware of their lifestyle patterns. However, when the information is recorded by hand it becomes difficult to organise the data and to identify simple trends.

The Health Analyser & Tracker is a console application written in Python which enables users to input their personal details and to keep a record of their daily health activities; it computes the BMI, stores the daily health records, calculates the average values, determines both the highest and lowest number of steps, carries out a basic health analysis and gives a health score.

It is being developed for educational use and is not to be used for medical diagnosis or treatment.

---

## 2. Objectives

1. To obtain basic information about the user.
2. To work out and show BMI.
3. Keep a record of the amount of water you take in each day, the number of steps you walk and the exercises you do.
4. So that you can store your daily health records multiple times.
5. To work out the average values for health-related activity.
To find the maximum and minimum number of steps.
7. To analyse the daily health records.
8. To work out a basic health score.
To produce a final health report.

---

## 3. Main Features

- User Profile
- BMI Calculation
- BMI Category
- Daily Health Tracking
- Multiple Record Storage
- Average Calculation
- Highest and Lowest Step Analysis
- Health Analysis
- Health Score
- Final Health Report
- Input Validation

---

## 4. Functional Requirements

### Profile Management

The system should collect:

- Name
- Age
- Height
- Weight

### BMI Calculation

The system must compute the BMI using the height and weight entered by the user and then show the appropriate BMI category.

### Daily Health Tracking

The system should allow the user to enter:

- Date
- Water intake in litres
- Sleep duration in hours
- Total number of steps
- Exercise duration in minutes

### Health Analysis

The system should:

- Work out the average amount of water taken in.
- Figure out the average amount of sleep.
- Calculate average steps.
- Find the average length of exercise.
- Find the greatest number of steps.
- Find the smallest number of steps.
- Look at the most recent health record.
- Work out a basic health score.

### Report Generation

The system must show the health records that have been stored and produce a final health report which includes the user's profile, their BMI information and the health data that has been recorded.

---

## 5. Input Validation

The program checks that:

- The age is more than zero.
- The height is more than zero.
- The weight is more than zero.
- Water intake is not negative.
- Sleep duration is not negative.
The number of steps is not negative.
Exercise duration is not less than zero.
- The program deals with invalid numerical input correctly.

---

## 6. Technologies Used

The project is developed in Python.

Python concepts used include:

- Functions
- Modules
- Lists
- Dictionaries
- Conditional Statements
- Loops
- Input Validation

---

## 7. Testing

The program must be tested with both valid and invalid inputs.

| Test Case | Input / Action | Expected Result |
|---|---|---|
| TC01 | Enter valid profile details | Profile is accepted and BMI is calculated |
| TC02 | Enter text instead of age | Invalid input message is displayed |
| TC03 | Enter zero or negative age | Invalid age is rejected |
| TC04 | Enter zero or negative height | Invalid height is rejected |
| TC05 | Enter zero or negative weight | Invalid weight is rejected |
| TC06 | Enter negative water intake | Value is rejected |
| TC07 | Enter negative sleep duration | Value is rejected |
| TC08 | Enter negative steps | Value is rejected |
| TC09 | Enter negative exercise duration | Value is rejected |
| TC10 | Choose option 1 and add a valid record | Daily record is stored |
| TC11 | Choose option 2 | Stored records are displayed |
| TC12 | Choose option 3 | Health analysis is displayed |
| TC13 | Select an invalid menu option | Invalid option message is displayed |
| TC14 | Choose option 4 | Final health report is displayed |

---

## 8. Future Scope

Possible future improvements include:

- Save the health records permanently to a file.
- Include graphs and charts to illustrate health trends.
- Including additional health analysis functions.
- Include a graphical user interface.
- Let users make edits to records.
Letting users remove individual records.
- Adding database storage.

---

## 9. Project Limitations

The project is an educational health-tracking application.

The health score is determined by a set of fixed thresholds which are defined in the program and must not be regarded as medical advice, a diagnosis or treatment.

The records are stored by the current version only while the program is running and it fails to offer permanent database storage.

---

## 10. Conclusion

The Health Analyser & Tracker shows how Python programming concepts can be put into practice when developing a simple health-tracking application.

Users are able to keep daily records of their health, work out their BMI, analyse their basic health information and produce a final health report. The project also shows how functions, modules, lists, dictionaries, loops, and input validation can be used.
