# --- First Method of openning a file ---
#f = open('test.txt', 'r')

#print(f.name)
#print(f.mode)

#f.close()

# ---Openning the file with context manager ---
#with open('test.txt', 'r') as f:
    
    #print(f.name)
    #print(f.mode)

    #f_contents = f.read()
    #print(f_contents)

    #f_contents = f.readline()
    #print(f_contents, end='')

#print(f.closed)

# --- Using loops for printing the lines --- 
#with open('test.txt', 'r') as f:
#    
#    for line in f:
#        print(line, end='')

#with open('test.txt', 'r') as f:
#    
#    size_to_read = 10
#    f_contents = f.read(size_to_read)
#
#    while len(f_contents) > 0:
#        print(f_contents, end='')
#        f_contents = f.read(size_to_read) #at the end of the file f.read returns an empty string
        
#with open('test.txt', 'r') as f:
#
#    size_to_read = 10
#    f_contents = f.read(size_to_read)
#    print(f_contents, end = '')
#    
#    f.seek(0)
#
#    f_contents = f.read(size_to_read)
#    print(f_contents)

# --- Working with multiple files ---
#with open('test.txt', 'r') as rf:
#    with open('test_copy.txt', 'w') as wf:
#        for line in rf:
#            wf.write(line)

# --- Copying an image ---
with open('monument.jpeg', 'rb') as rf:
    with open('monument_copy.jpeg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
