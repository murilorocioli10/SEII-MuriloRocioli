# Code 01
num = 3
print(type(num))

num = 3.14
print(type(num))

# Arithmetic Operators 
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2) # floor division
print(3 % 2)  # modulus (remainder)
print(3 ** 2) # exponent
print(3 * 2 + 1)
print(3 * (2 + 1))

# Incrementing Values
num = 1
num = num + 1 #2
num += 1      #2
num *= 10     #10
print(num)

print(abs(-3))       #absolute value de 3
print(round(3.75))   #round to 4 
print(round(3.75,1)) #second argument is the digit after the decimal

# Comparisons Operators
num_1 = 3
num_2 = 2
print(num_1 == num_2)   #false
print(num_1 != num_2)   #true
print(num_1 > num_2)    #true
print(num_1 < num_2)    #false
print(num_1 >= num_2)   #true
print(num_1 <= num_2)   #false

# Strings to numbers
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)    #concatenates num_1 and num_2 100200
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)    #300
