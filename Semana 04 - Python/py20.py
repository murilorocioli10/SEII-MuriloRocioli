# Code 01
try:
    f = open('test_file.txt')
    #var = bad_var #causes an error
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception as e:
    print(e)

# Code 02
try:
    f = open('curruptfile.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')
