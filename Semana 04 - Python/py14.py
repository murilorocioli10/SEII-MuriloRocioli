import os

os.chdir("/home/murilo/Documents/GitHub/SEII-MuriloRocioli/Semana 04 - Python/py14/txt_files")
#print(os.getcwd())
#print(os.listdir())

for f in os.listdir():

    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    
    f_title = f_title.strip()   #the strip() method remove the spaces
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) 

    #print('{}-{}-{}{}'. format(f_num, f_course, f_title,f_ext))
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    print(new_name)

    os.rename(f, new_name)
