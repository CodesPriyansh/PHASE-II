class Student:
    def __init__(self, name, age, rollNo, classSec, majorSubject, grades):
        self.name = name
        self.age = age 
        self.rollNo = rollNo
        self.classSec = classSec
        self.majorSubject = majorSubject
        self.grades = grades
     

class Course:
    def __init__(self, maxStudents):
        self.maxStudents = maxStudents
        self.students = []  
        
    def add_student(self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return "student added successfully."
        else:
            return "Maximum number of students reached."
    
    def personal_record(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return f"Name: {student.name}, Age: {student.age}, Roll No: {student.rollNo}, Class: {student.classSec}, Major Subject: {student.majorSubject}, Grades: {student.grades}"
                
        return "student not found."
        
    def update_student_information(self, student_name, name=None, age=None, rollNo=None, classSec=None, majorSubject=None, grades=None):
        for student in self.students:
            if student.name == student_name:
                if name is not None:
                    student.name = name
                if age is not None:
                    student.age = age
                if rollNo is not None:
                    student.rollNo = rollNo
                if classSec is not None:
                    student.classSec = classSec
                if majorSubject is not None:
                    student.majorSubject = majorSubject
                if grades is not None:
                    student.grades = grades
                
                return f"Student:{student_name} Information Updated Successfully."
        return "Student Not Found."
    
    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student) 
                return f"Student:{student_name} removed successfully."
        return "student not found."
    
    def average_grade(self):
        total_grades = sum(student.grades for student in self.students)
        return total_grades / len(self.students)
    
    def average_age(self):
        total_age = sum(student.age for student in self.students)
        return total_age / len(self.students) 
    
# Create instances of students
s1 = Student("alice", 18, 21, "XII-H", "History", 70)
s2 = Student("jill", 17, 2, "XI-H", "Sociology", 95)
s3 = Student("tristan", 20, 30, "XII-A", "History", 80)

# Create a course and add students to it
course = Course(2)
print(course.add_student(s1))  # Should succeed
print(course.add_student(s2))  # Should succeed
print(course.add_student(s3))  # Should fail, as max students is 2

# Get personal records
record1 = course.personal_record("alice")
record2 = course.personal_record("jill")
record3 = course.personal_record("tristan")
print(record1)
print(record2)
print(record3)

# Update student information
print(course.update_student_information("alice", age=17, rollNo=34))

# Get updated personal record
record_new = course.personal_record("alice")
print(record_new)

# Remove a student
print(course.remove_student("jill"))

# Try to get the record of the removed student
record_removed = course.personal_record("jill")
print(record_removed) 

print(f"Average Grade: {course.average_grade()}")
print(f"Average Age: {course.average_age()}") 