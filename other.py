class employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        print("Заробітня плата", self.name + ":", self.salary)\

emp = employee("Саша", "Менеджер", 25000)

print("Name-", emp.name)
print("Position-", emp.position)
print("Salary-", emp.salary)

emp.get_salary_info()