def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"
    
students_data={}
while True:
    name=input("Enter Student's Name:").strip()
    roll_Number=input("Enter Student's Roll Number:").strip()

    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                marks[subject]=int(input(f"Enter the Marks of {subject}:"))
                if 0 <= marks[subject] <= 100:
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid Input! Please Enter A Number")
        

    total_marks = sum(marks.values())
    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)

    students_data[roll_Number] = {
        "name": name,
        "marks": marks,
        "total": total_marks,
        "percentage": percentage,
        "grade": grade,
    }

    more = input("Do you want to insert more? Press 'Y' for Yes or 'N' for No: ").strip().upper()
    if more == "N":
        break

# Displaying student reports
print("\n📄 Student Report Cards:")
print("="*50)
for roll, data in students_data.items():
    print(f"\n🎓 Student: {data['name']} (Roll No: {roll})")
    print("-"*40)
    for subject, marks in data["marks"].items():
        print(f"{subject}: {marks}")
    print("-"*40)
    print(f"Total Marks: {data['total']} / 500")
    print(f"Percentage: {data['percentage']:.2f}%")
    print(f"Grade: {data['grade']}")
    print("="*50)

# The Logic Of this code:
# Collects student details and stores them in a dictionary (students_data).
# Validates marks (ensures input is numeric and between 0-100).
# Computes total marks, percentage, and assigns a grade.
# Asks if the user wants to enter another student.
# After input ends, displays report cards for all students.




 