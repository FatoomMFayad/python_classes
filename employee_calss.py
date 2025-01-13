class Employee:
    id = ''
    name = ''
    basic_salary = 0
    is_married = False
    has_insurance = False
    no_children = 0
    job_title = ''

p1 = Employee()
p2 = Employee()
p3 = Employee()

p1.id = '1'
p1.name = 'Fatoom'
p1.basic_salary = 10000
p1.is_married = False
p1.has_insurance = True
p1.no_children = 0
p1.job_title = 'Team Leader'

p2.id = '2'
p2.name = 'Hanan'
p2.basic_salary = 15000
p2.is_married = True
p2.has_insurance = True
p2.no_children = 3
p2.job_title = 'Hospital Manager'

p3.id = '3'
p3.name = 'Basma'
p3.basic_salary = 50000
p3.is_married = True
p3.has_insurance = True
p3.no_children = 5
p3.job_title = 'Minister'


employees = [p1, p2, p3]

for employee in employees:
    print(employee.name, employee.job_title)

