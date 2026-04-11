class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("NAME:",self.name)
        print("AGE: ",self.age)
per=student("harathi",18)
print(per.name)
per.display()
