class Workers():
    def __init__(self,name,fname,salary):
        self.name = name
        self.fname = fname
        self.salary = salary
        self.email = name + fname + "@company.com"

    def show_info(self):
        return f"Name: {self.name} Surname: {self.fname} Salary: {self.salary} Email: {self.email} "    

worker1 =  Workers("Ali","Guzel",5000)
worker2 = Workers("Hasan","Mutlu",8000) 

class Programmer(Workers):
    pass


programmer1 = Programmer("Jenny","Leila",9000)
programmer2= Programmer("Fatma","Yildiz",9000)

print(programmer1.name)
print(programmer2.fname)
print(worker1.email)
print(programmer2.show_info())
#---------------------------------------------------------------------------------------


