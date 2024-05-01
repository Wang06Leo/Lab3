# test_employee_info.py

import employee_info

def test_get_employees_by_age_range():
    # Test case: age range from 25 to 35
    result = employee_info.get_employees_by_age_range(10, 50)
    expected_result = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    assert result == expected_result

def test_calculate_average_salary():
    # Test case: average salary calculation
    average_salary = employee_info.calculate_average_salary()
    assert average_salary == (50000+60000+56000+70000+65000+60000)/6

def test_get_employees_by_dept():
    # Test case: employees in the Sales department
    result = employee_info.get_employees_by_dept("Sales")
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    assert result == expected_result

    # Test case: employees in the Engineering department
    result = employee_info.get_employees_by_dept("Engineering")
    expected_result = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert result == expected_result
