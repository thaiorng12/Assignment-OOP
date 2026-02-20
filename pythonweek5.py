class Employee:
    def __init__(self, name,age, salary):
        self.name = name            # public attribute
        self._age = age             # protected with only one _
        self.__salary = salary      # private attribute with two __
    def show_salary(self) -> None:
        print("Salary:", self.__salary)
emp = Employee("Fedrick",30, 50000)
print(emp._age)
emp.show_salary()