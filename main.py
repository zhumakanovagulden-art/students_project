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


def add_student(name):
    students.append(name)
    print(f"Жаңа студент қосылды: {name}")

def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"Студент удален: {name}")
    else:
        print(f"Студент не найден: {name}")
        
show_students()
search_student("Гүлден")
add_student("Ержан")
remove_student("Ержан")
show_students()