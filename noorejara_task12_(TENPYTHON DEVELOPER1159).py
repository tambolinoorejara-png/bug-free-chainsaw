import csv

# 1 & 2. Create 'student.csv' and store details of 10 students with 4 subjects
student_data = [
    {"Roll No": "101", "Name": "Aarav Sharma", "Maths": 85, "Physics": 78, "Chemistry": 92, "English": 88},
    {"Roll No": "102", "Name": "Ananya Patel", "Maths": 92, "Physics": 85, "Chemistry": 89, "English": 94},
    {"Roll No": "103", "Name": "Isha Gupta", "Maths": 74, "Physics": 80, "Chemistry": 76, "English": 82},
    {"Roll No": "104", "Name": "Kabir Singh", "Maths": 98, "Physics": 95, "Chemistry": 96, "English": 91},
    {"Roll No": "105", "Name": "Mira Nair", "Maths": 68, "Physics": 72, "Chemistry": 70, "English": 75},
    {"Roll No": "106", "Name": "Rohan Verma", "Maths": 81, "Physics": 84, "Chemistry": 79, "English": 80},
    {"Roll No": "107", "Name": "Sai Reddy", "Maths": 89, "Physics": 91, "Chemistry": 85, "English": 87},
    {"Roll No": "108", "Name": "Siddharth Joshi", "Maths": 77, "Physics": 65, "Chemistry": 73, "English": 79},
    {"Roll No": "109", "Name": "Tanvi Rao", "Maths": 93, "Physics": 88, "Chemistry": 91, "English": 90},
    {"Roll No": "110", "Name": "Vihaan Das", "Maths": 62, "Physics": 58, "Chemistry": 64, "English": 70}
]

filename = "student.csv"
fields = ["Roll No", "Name", "Maths", "Physics", "Chemistry", "English"]

# Writing to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(student_data)

print(f"--- '{filename}' created successfully ---\n")


# 3. Read the CSV file and display all student records
print(f"{'Roll No':<10}{'Name':<20}{'Maths':<8}{'Physics':<10}{'Chemistry':<12}{'English':<8}{'Total':<8}")
print("-" * 75)

highest_marks = -1
highest_scorer = ""
total_marks_all_students = 0
total_subjects_count = 0

with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Extract fields and convert marks to integers
        roll_no = row["Roll No"]
        name = row["Name"]
        m1 = int(row["Maths"])
        m2 = int(row["Physics"])
        m3 = int(row["Chemistry"])
        m4 = int(row["English"])
        
        # Calculate total for current student
        student_total = m1 + m2 + m3 + m4
        
        # Display student row
        print(f"{roll_no:<10}{name:<20}{m1:<8}{m2:<10}{m3:<12}{m4:<8}{student_total:<8}")
        
        # 4. Logic to track the student with the highest total marks
        if student_total > highest_marks:
            highest_marks = student_total
            highest_scorer = name
            
        # Accumulate metrics for calculating overall average later
        total_marks_all_students += student_total
        total_subjects_count += 4

print("-" * 75)

# 4. Display the student who scored the highest marks
print(f"\nTop Scorer: {highest_scorer} with a total of {highest_marks} marks.")

# 5. Calculate and display the average marks of all students
# (Average = Total marks scored by all students combined / Grand total number of individual subject papers)
overall_average = total_marks_all_students / total_subjects_count
print(f"Average Marks of all students across all subjects: {overall_average:.2f}")
