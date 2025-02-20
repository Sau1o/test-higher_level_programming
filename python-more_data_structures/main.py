#!/usr/bin/python3
filtering_data = __import__('17-filtering_data').filtering_data

employees = [
    {'name': 'João', 'age': 35, 'job': 'Manager', 'salary': 15000},
    {'name': 'Maria', 'age': 27, 'job': 'Director', 'salary': 8000},
    {'name': 'Pedro', 'age': 42, 'job': 'Diretor', 'salary': 20000},
    {'name': 'Ana', 'age': 31, 'job': 'Analyst', 'salary': 12000},
    {'name': 'Lucas', 'age': 29, 'job': 'Analyst', 'salary': 9000}
]

high_salary_names = filtering_data(employees)

print(high_salary_names)
 
