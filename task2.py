# class 1: Student
class Student:
    def __init__(self, rollno, marks):
        self.rollno = rollno  
        self.marks = marks
        obj = Student("23", "98")
    def learning(self):
        print(f"Student {self.rollno} is learning.")

# class 2: Bank
class Bank:
    def __init__(self, bank_balance, account_num):
        self.bank_balance = bank_balance 
        self.account_num = account_num  
        obj = Bank("34566", "123456789") 
        
    def banking(self):
        print(f"Accessing account: {self.account_num}")

# class 3: Room
class Room:
    def __init__(self, roommate, beds):
        self.roommate = roommate
        self.beds = beds    
        obj = Room("Alex", 2)             
       
    def cleaning(self):
        print("Cleaning the room...")

# class 4: Hotel
class Hotel:
    def __init__(self, customer_name, order):
        self.customer_name = customer_name
        self.order = order    
        obj = Hotel("John Doe", "Pizza")         
        
    def booking(self):
        print(f"Booking for {self.customer_name} confirmed.")

# class 5: Home
class Home:
    def __init__(self, location, layout):
        self.location = location
        self.layout = layout
        obj = Home("New York", "3BHK")
        
    def calculate_area(self):
        print(f"Calculating area for layout: {self.layout}")


