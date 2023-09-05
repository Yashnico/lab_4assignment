class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}\nName: {self.name}\nAge: {self.age}\nSalary: {self.salary}\n"

def search_employee(employees, search_parameter, search_value):
    results = []
    if search_parameter == 1:  
        results = [emp for emp in employees if emp.age == int(search_value)]
    elif search_parameter == 2:  
        results = [emp for emp in employees if emp.name.lower() == search_value.lower()]
    elif search_parameter == 3:  
        operator = input("Enter the comparison operator (<, >, <=, >=): ")
        if operator in ['<', '>', '<=', '>=']:
            results = [emp for emp in employees if eval(f"emp.salary {operator} {search_value}")]
        else:
            print("Invalid operator!")
    else:
        print("Invalid search parameter!")

    return results

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

search_param = int(input("Enter the search parameter (1. Age, 2. Name, 3. Salary): "))
search_value = input("Enter the search value: ")

results = search_employee(employees, search_param, search_value)
if results:
    print(f"Search Results ({len(results)}):")
    for emp in results:
        print(emp)
else:
    print("No results found.")