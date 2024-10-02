 # Write a program to create a class with name Student and perform the following tasks - Declare a variable grade Print a sentence inside the class Create an object of class student and see the output

class Student:
    # Attribute
    grade = 9

    # Method
    def display(self):
        print("Student graade is", self.grade)

# MAIN PROGRAM
# Create an object
student1 = Student()
student1.display()