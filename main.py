students = ["Назым", "Асем", "Гүлден", "Жаннур", "Айгерим"]


def show_students():
    print("Студенттер тізімі:")
    for student in students:
        print(student)


def search_student(name):
    if name in students:
        print(f"Студент табылды: {name}")
    else:
        print(f"Студент табылмады: {name}")


show_students()
search_student("Гүлден")