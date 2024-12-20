student = {}
def add_student():
    student_id =input("ENTER STUDENT ID :")
    if student_id in student:
        print(" student already exixt")
        return
    mark = {}
    while True:
        subject = input("enter sujbect (or  'done ' to finish):")
        if subject.lower() == 'done':
             break
        mark[subject]=int(input(f"enter mark for the {subject}: "))
    student[student_id] = mark
    print("student Added successfully")
    
def update_student():
    student_id = input("ENTER STUDENT ID  TO UPDATE:")
    if student_id not in student:
        print("student does not exist")
        return
    mark =student[student_id]
    while True:
        subject = input("enter sujbect (or  'done ' to finish):")
        if subject.lower() == 'done':
            break
        mark[subject]=int(input(f"ENTER MARK FOR {subject}:"))
        student[student_id] = mark
        print("student updated successfully")
1
def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in student:
        del student[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def display_results():
    if not student:
        print("No records to display!")
        return
    results = []
    for student_id, marks in student.items():
        total = sum(marks.values())
        percentage = total / len(marks) if marks else 0
        results.append((student_id, total, percentage))
    results.sort(key=lambda x: x[1], reverse=True)
    
    print("\nRank | Student ID | Total Marks | Percentage")
    for rank, (student_id, total, percentage) in enumerate(results, 1):
        print(f"{rank:<5} {student_id:<11} {total:<12} {percentage:.2f}%")

while True:
    print("\n1. Add Student\n2. Update Student\n3. Delete Student\n4. Display Results\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        display_results()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again!")
