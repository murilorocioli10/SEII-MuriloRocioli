student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
print(student['name'])      #John
print(student['courses'])   #['Math', 'CompSci']
print(student['age'])       #25
print(student.get('name'))  #John
print(student.get('phone')) #none
print(student.get('phone', 'Not Found')) #Not Found

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student) #{'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student) #{'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
del student['age']
print(student) #{'name': 'John', 'courses': ['Math', 'CompSci']}

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
age = student.pop('age')
print(age) #25
print(len(student)) #2

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
print(student.keys())   #dict_keys(['name', 'age', 'courses'])
print(student.values()) #dict_values(['John', 25, ['Math', 'CompSci']])
print(student.items())  #dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])
for key,value in student.items():
    print(key,value)
