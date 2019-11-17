# Person.py
#
# Person is a class that defines a citizen with a name.  
# Students and Employees are subclasses of Persons.
# Usage:
#      % python Person.py 
#
# Himanshu Mohan, Nov 12, 2019

class Person:
    "People have a first and last name"
    
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname

    def __eq__(self, other):
        #return (self.firstname == other.firstname) and (self.lastname == other.lastname)
        return ((self.firstname).lower() == (other.firstname).lower())and((self.lastname).lower() == (other.lastname).lower())
    def is_employed(self):
        return False


class Student(Person):
    "Person who is a student"

    def __init__(self, first, last, school, id):
        # Call Superclass to set common information
        super().__init__(first, last)
        self.school = school
        self.id = id

    def __str__(self):
        # Call Superclass to dispaly common information
        return super().__str__() + ", " + str(self.id) + ' at ' + self.school

    def __eq__(self, other):
        return super().__eq__(other) and (self.id == other.id) and (self.school == other.school)
    
    def is_employed(self):
        return False

class Employee(Person):
    "Person who is employed"
    def __init__(self, first, last, company, id):
        #pass
        # Call Superclass to set common information
        super().__init__(first, last)
        self.company = company
        self.id = id
        
    def __str__(self):
        # Call Superclass to dispaly common information
        return super().__str__() + ", " + str(self.id) + ' at ' + self.company
    
    def __eq__(self, other):
        return super().__eq__(other) and (self.id == other.id) and (self.company == other.company)
        
    def is_employed(self):
        return True