

## Student Admission System

students = []

while True:
    print("\n School Admission System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter grade applying for: ")
        contact = input("Enter parent contact number: ")
        if len(contact) == 10 and contact.isdigit():
            students.append({
                "Name": name,
                "Age": age,
                "Grade": grade,
                "Contact": contact
            })
            print(" Student added successfully!")
        else:
            print(" Contact number must be exactly 10 digits.")

    

    elif choice == "2":
        if not students:
            print("No students admitted yet.")
        else:
            print("\n--- Student Admissions ---")
            for i, s in enumerate(students, start=1):
                print(f"{i}. {s['Name']} | Age: {s['Age']} | Grade: {s['Grade']} | Contact: {s['Contact']}")

    elif choice == "3":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")






