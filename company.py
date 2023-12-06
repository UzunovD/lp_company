"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""
from math import inf

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


# Уровень 1
# # 1. Вывести названия всех отделов
for department in departments:
    print(department['title'])

# # 2. Вывести имена всех сотрудников компании.
for department in departments:
    for employer in department['employers']:
        print(f'{employer['first_name']} {employer['last_name']}')

# # 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
for department in departments:
    for employer in department['employers']:
        print(f"{employer['first_name']} {employer['last_name']} department: {department['title']}")

# # 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 100_000:
            print(f"{employer['first_name']} {employer['last_name']}")

# # 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] < 80_000:
            print(f"{employer['position']}")

# # 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
for department in departments:
    salary_by_department = 0
    for employer in department['employers']:
        salary_by_department += employer['salary_rub']
    print(f"salary_by_department for {department['title']} = {salary_by_department}")

# Второй уровень
# # 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
for department in departments:
    min_salary = inf
    for employer in department['employers']:
        if employer['salary_rub'] < min_salary:
            min_salary = employer['salary_rub']
    print(f"min_salary_by_department for {department['title']} = {min_salary}")

# # 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
for department in departments:
    max_salary = -inf
    min_salary = inf
    total_salary = 0
    for employer in department['employers']:
        if employer['salary_rub'] < min_salary:
            min_salary = employer['salary_rub']
        if employer['salary_rub'] > max_salary:
            max_salary = employer['salary_rub']
        total_salary += employer['salary_rub']
        average_salary = total_salary/len(department['employers'])
    print(f"{department['title']} {min_salary=} {max_salary=} {average_salary=}")

# # 9. Вывести среднюю зарплату по всей компании.
total_salary = 0
total_employer = 0
for department in departments:
    for employer in department['employers']:
        total_salary += employer['salary_rub']
        total_employer += 1
average_salary_by_company = total_salary / total_employer
print(f"{average_salary_by_company=}")

# # 10. Вывести названия должностей, которые получают больше 90к без повторений.
positions = set()
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 90_000:
            positions.add(employer['position'])
print(', '.join(positions))

# # 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
employers = ('Michelle', 'Nicole', 'Christina', 'Caitlin')
for department in departments:
    total_salary = 0
    total_employers = 0
    for employer in department['employers']:
        if employer['first_name'] in employers:
            total_salary += employer['salary_rub']
            total_employers += 1
    print(f"average salary by girls fo {department['title']}={total_salary/total_employers:.2f}")

# # 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
employers = []
for department in departments:
    for employer in department['employers']:
        if employer['last_name'][-1] in 'euioa':
            employers.append(employer['first_name'])
print(', '.join(employers))


#Третий уровень:
# # 13. Вывести список отделов со средним налогом на сотрудников этого отдела.
for department in departments:
    tax_by_depart = 0
    for tax in taxes:
        if not tax['department'] or tax['department'] == department['title']:
            tax_by_depart += tax['value_percents']
    print(f"{department['title']} {tax_by_depart=}")

# # 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
for department in departments:
    for employer in department['employers']:
        tax_by_employer = 0
        for tax in taxes:
            if not tax['department'] or tax['department'] == department['title']:
                tax_by_employer += tax['value_percents']
        net_salary = employer['salary_rub'] * (1 - tax_by_employer / 100)
        print(f"{employer['first_name']} {employer['last_name']} gross salary = {employer['salary_rub']}, "
              f"net salary = {net_salary:.2f}")

# # 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
res = {}
for department in departments:
    tax_by_depart = 0
    for tax in taxes:
        if not tax['department'] or tax['department'] == department['title']:
            tax_by_depart += tax['value_percents']
    res[department['title']] = tax_by_depart
for k, v in sorted(res.items(), key=lambda item: item[1]):
    print(k)

# # 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
for department in departments:
    for employer in department['employers']:
        tax_by_employer = 0
        for tax in taxes:
            if not tax['department'] or tax['department'] == department['title']:
                tax_by_employer += tax['value_percents']
        tax_amount = employer['salary_rub'] * tax_by_employer / 100
        if tax_amount * 12 > 100_000:
            print(f"{employer['first_name']} {employer['last_name']}")

# # 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
res = {}
for department in departments:
    for employer in department['employers']:
        tax_by_employer = 0
        for tax in taxes:
            if not tax['department'] or tax['department'] == department['title']:
                tax_by_employer += tax['value_percents']
        tax_amount = employer['salary_rub'] * tax_by_employer / 100
        res[f"{employer['first_name']} {employer['last_name']}"] = tax_amount
res = sorted(res.items(), key=lambda item: item[1])
print(res[0][0])
