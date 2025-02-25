
dept_data = {
    101: [(1, 50000), (2, 60000), (3, 55000)],  
    102: [(4, 70000), (5, 75000), (6, 72000)],
    103: [(7, 40000), (8, 45000), (9, 42000)],  
}


def find_min_max_salary(dept_data):
    for dept_no, employees in dept_data.items():
        salaries = [salary for roll_no, salary in employees]
        min_salary = min(salaries)
        max_salary = max(salaries)
        print(f"Department {dept_no} - Min Salary: {min_salary}, Max Salary: {max_salary}")


find_min_max_salary(dept_data)
