# Function 01
def hello_func():
    pass        #The pass command line its useful for not having any erros at a empty function

# Function 02
def hello_func():
    print('Hello Function')

print(hello_func)   #Result: <function hello_func at 0x7fc533f660d0
print(hello_func()) #Result: None
hello_func()        

# Function 03
def hello_func():
    return 'Hello Function'

print(len(hello_func()))
print(hello_func().upper())


# Function 04
def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting,name)

print(hello_func('Hi', name = 'Corey'))

# Function 05
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
student_info(*courses, **info) #adding the *, the arguments are unpacked

#5) Function 06
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))
print(days_in_month(2017, 2))
