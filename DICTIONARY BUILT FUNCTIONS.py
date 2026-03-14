student={"name":"harathi","age":19,"course":"python"}
print("Originaldictionary:",student)
print("keys:",student.keys())
print("values:",student.values())
print("items:",student.items())
print("get value:",student.get("name"))
print("pop:",student.pop("course"))

student.update({"age":21})
print("After update:",student)
print("clear:",student.clear())
