#creating object to one class and pass that object as arguments into another class is called aggregation.

class Student:
    def __init__(self):
        self.__name = None
        self.__rollno = 0
        self.__marks = []
        self.__total = 0
        self.__avg = 0.0
    def setinfo(self):
        self.__name = input('Enter Name: ')
        self.__rollno = int(input('Enter Roll No: '))
        self.__marks = map(int,input('Enter Marks').split())
        self.__total = sum(self.__marks)
        self.__avg = self.__total/5
    def getinfo(self):
        print('Student Name: ',self.__name)
        print('Student Roll No: ',self.__rollno)
        print('Total: ',self.__total)
        print('Average: ',self.__avg)

class College:
    def __init__(self,other):
        self.__dept = None
        self.__sem = None
        self.__year = 0
        self.__stu = other
    def set_college(self):
        self.__stu.setinfo()
        self.__dept = input('Enter Department: ')
        self.__sem = input('Enter Semester: ')
        self.__year = input('Enter Year: ')
    def get_college(self):
        self.__stu.getinfo()
        print('Department: ',self.__dept)
        print('Year: ',self.__year)
        print('Semester: ',self.__sem)

stu = Student()
col = College(stu)
col.set_college()
col.get_college()
#del col
#print("college object is deleted")
#stu.getinfo()


#simple aggregation program       #both the objects are able to survive individually

class Salary:
	def __init__(self,pay,bonus):
		self.pay=pay
		self.bonus=bonus
	def annual_salary(self):
		return (self.pay*12) + self.bonus
class employee:
	def __init__(self,name,age,salary):
		self.empname=name
		self.empage=age
		self.obj_salary=salary
	def total_salary(self):
		print("successfully")
		return self.obj_salary.annual_salary()
salary=Salary(1000,1500)
emp=employee('durga',25,salary)
print(emp.total_salary())
del emp
print(salary.annual_salary())


#composition

class Salary:
	def __init__(self,pay,bonus):
		self.pay=pay
		self.bonus=bonus
	def annual_salary(self):
		return (self.pay*12) + self.bonus
class employee:
	def __init__(self,name,age,pay,bonus):
		self.empname=name
		self.empage=age
		self.obj_salary=Salary(pay,bonus)
	def total_salary(self):
		print("successfully")
		return self.obj_salary.annual_salary()

emp=employee('durga',25,1500,1000)
print(emp.total_salary())


