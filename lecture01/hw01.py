class Student():
    def __init__(self,student_id,name,age):
        self.student_id=student_id
        self.name=name
        self.age=age
    
    def display_info(self):
        print(f"ID: {self.student_id}번 / 이름: {self.name} / 나이: {self.age}살")

class StudentManager():
    def __init__(self):
        self.students=[]
    
    def add_student(self,student):
        self.students.append(student)

    def display_all_students(self):
        for s in self.students:
            Student.display_info(s)

s1=Student(1,"김철수",20)
s2=Student(2,"이영희",21)
s3=Student(3,"박지민",19)

s_manager=StudentManager()
s_manager.add_student(s1)
s_manager.add_student(s2)
s_manager.add_student(s3)

print("현재 등록된 학생 목록:")
s_manager.display_all_students()
print()

s4=Student(4,"한지수",22)
s_manager.add_student(s4)

print("학번 4번 학생 추가 후:")
s_manager.display_all_students()
