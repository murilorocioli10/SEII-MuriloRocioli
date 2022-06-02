# Code 01
print('Hello world')

# Code 02
message = 'Hello World'
print(message)

# Code 03
message = 'Bobby\'s World'
print(message)

# Code 04
message = "Bobby's World"
print(message)

# Code 05
message = """Bobby's World was a good cartoon in the 1990s"""
print(message)

# Code 06
message = 'Hello World'
print(len(message))

# Code 07
message = 'Hello World'
print(message[10])

# Code 08
message = 'Hello World'
print(message[0:5])

message = 'Hello World'
print(message[:5])

# Code 09
message = 'Hello World'
print(message.lower())

# Code 10
message = 'Hello World'
print(message.upper())

# Code 11
message = 'Hello World'
print(message.count('Hello'))
print(message.count('l'))

# Code 12
message = 'Hello World'
print(message.find('Hello'))
print(message.find('World'))

# Code 13
message = 'Hello World'
new_message = message.replace('World','Universe')
print(new_message)

# Code 14
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'
print(message)

# Code 15
greeting = 'Hello'
name = 'Michael'
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

# Code 16
greeting = 'Hello'
name = 'Michael'
message = f'{greeting}, {name.upper()}. Welcome!' #fstrings
print(message)

# Code 17
greeting = 'Hello'
name = 'Michael'
print(dir(name))

# Code 18
greeting = 'Hello'
name = 'Michael'
print(help(str.lower))
