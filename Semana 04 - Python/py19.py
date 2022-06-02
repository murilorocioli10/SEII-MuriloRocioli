#1)
# li = [9,1,8,2,7,3,6,4,5]

# s_li = sorted(li)
# # s_li = sorted(li, reverse=True)
# # s_li = li.sort() #formato errado

# print('Sorted Variable:\t', s_li) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# li.sort()
# # li.sort(reverse=True)
# print('Original Variable:\t', li) #[1, 2, 3, 4, 5, 6, 7, 8, 9], n precisa criar uma nova variavel

#2) 
# tup = (9,1,8,2,7,3,6,4,5)
# # tup.sort() #erro
# s_tup = sorted(tup)
# print('Tuple\t', s_tup)

# di = {'name': 'Corey', 'Job': 'programming', 'age': None, 'os': 'Mac'}
# s_di = sorted(di)
# print('Dict\t', s_di) 

#3)
# li = [-6,-5,-4,1,2,3]
# s_li = sorted(li, key=abs)
# print(s_li)

#4)
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort, reverse = True)

print(s_employees)
