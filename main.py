import pandas as pd
data = {"name": ["youssef","ahmed"],"salary": [10000,7000]}
df = pd.DataFrame(data)
print (df)


import json
with open("employee.json", "r") as f:
    data = json.load(f)

employees = data["employees"]
employees[0]["salary"] = 12000  
data["employees"] = employees
with open("employee.json", "w",) as f:
    json.dump(data, f, indent=4)
for employee in employees:
    print (employee["name"], employee["salary"], employee["job"])
for employee in employees:
    if employee["salary"]>=10000:
        print (employee["name"])
total_salary = sum(employee["salary"] for employee in employees)
average_salary = total_salary / len(employees)
print( average_salary)
r= json.dumps(employees[0], indent=4)
print (r)

print ("my first github project")