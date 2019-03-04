class employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department


emp1 = employee("Vibhav", "Cient Flows")
emp2 = employee("Graffy","Self Employed")

print(emp1.name + " " + emp1.department)
print(emp2.name + " " + emp2.department)