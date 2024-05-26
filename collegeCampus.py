#create the base class
class Person:
    #create common attributes
    def __init__(self, name, age, id_number, email):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.email = email
        
    #create a method to return basic information about the person.
    def get_details(self):
        return f"name: {self.name}, age: {self.age}, id number: {self.id_number}, email: {self.email}."
    
#creating derived class - Faculty
class Faculty(Person):
    #creating attributes and initializing common attributes using super
    def __init__(self, name, age, id_number, email, department, position):
        Person.__init__(self, name, age, id_number, email)
        self.department = department
        self.position = position 
    
    #additional methods
    def teach_course(self):
        return f"{self.name} is a {self.position} who teaches {self.department}." 
    
    def publish_papers(self, paper_title, paper_source):
        return f"{paper_title} was published by {self.name} on {paper_source}."
        
#creating derived class - Staff
class Staff(Person):
    #creating attributes and initializing common attributes using super
    def __init__(self, name, age, id_number, email, department, role):
        Person.__init__(self, name, age, id_number, email)
        self.department = department
        self.role = role
        
    #additional methods
    def perform_duties(self):
        return f"{self.name} is from the department of: {self.department} with the role of {self.role}."
    
#creating derived class - Students
class Students(Person):
    #creating attributes and initializing common attributes using super
    def __init__(self, name, age, id_number, email, major, year):
        Person.__init__(self, name, age, id_number, email)
        self.major = major
        self.year = year
        
    #additional methods
    def attend_class(self, class_name):
        return f"{self.name} is attending class: {class_name}."
    
    def sumbit_assignment(self, assignment_name):
        return f"{self.name} has submitted the assignment '{assignment_name}'."
    
    
#creating instances 
s1 = Students("Jill", 19, "SF786", "callmejill@gmail.com", "Sociology", "Freshmen")
f1 = Faculty("Alice", 25, "FC999", "alice@umbrellacorp.com", "Bio-Tech", "Professor")
s2 = Staff("Miku", 24, "ST440", "yourwaifumiku@outlook.com", "Administration", "Administrator")

#using the methods

print(f1.get_details())
print(f1.teach_course())
print(f1.publish_papers("The Walking Dead", "Racoon City Times"))

print(s1.get_details())
print(s1.attend_class("social reforms"))
print(s1.sumbit_assignment("rich and poor"))

print(s2.get_details())
print(s2.perform_duties())  












