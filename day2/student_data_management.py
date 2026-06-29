students = ["Ali", "Sara", "Raj"]

student_data = {
    "Ali": {"marks": 88, "subject": "Math"},
    "Sara": {"marks": 72, "subject": "Science"},
    "Raj": {"marks": 55, "subject": "Math"}
}

unique_subjects = set()

for name in students:
    data = student_data[name]

    unique_subjects.add(data["subject"])

    if data["marks"] >= 80:
        grade = "A"
    elif data["marks"] >= 65:
        grade = "B"
    else:
        grade = "C"

    print(name, "| Marks:", data["marks"], "| Grade:", grade)

print("Subjects taught:", unique_subjects)