language = 'Python'

# if-else statement
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

# elif statement
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

# Using the and operator
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Using the not operator
user = 'Admin'
logged_in = False
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b) #True
print(a is b) #False -> 'is' looks for the same ID, same object in memory

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
