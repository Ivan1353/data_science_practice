import pandas as pd
import pandas_practice

data = [['9001','Jeff Russell', 'sales'],
        ['9002','Jane Boorman', 'sales'],
        ['9003','Tom Heints', 'sales']]
emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])
column_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(column_types)
emps = emps.set_index('Empno')

new_salary = pd.Series({"Salary": 5000}, name=9005)
new_emp = pd.Series({"Name": "John Hardy", "Job":"Sales"}, name = 9004)

salary = salary.append(new_salary)
emps = emps.append(new_emp)

emps_salary_left =  emps.join(salary, how="left")
emps_salary_right = emps.join(salary, how="right")
emps_salary_inner = emps.join(salary, how="inner")
emps_salary_outer = emps.join(salary, how ="outer")