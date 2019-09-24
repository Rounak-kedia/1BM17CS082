class Student:
	def __init__(self):
		self.id = None
		self.age = None
		self.marks = None

	def val_marks(self):
		return self.marks >= 0 and self.marks <=100

	def val_age(self):
		return self.age>20

	def check_qual(self):
		if(self.val_marks() and self.val_age()):
			return self.marks>=65
		print("\nData NOT Valid.")
		return False
	    
	def set(self):
		self.id = input("ID : ")
		self.age = int(input("AGE : "))
		self.marks = float(input("MARKS : "))

	def get(self):
		print("ID : ",self.id)
		print("AGE : ",self.age)
		print("MARKS : ",self.marks)

S = Student()
S.set()
S.get()
if S.check_qual():
    print("\nThe Student is qualified for admission.")
else:
    print("\nThe Student is NOT qualified for admission.")
    
