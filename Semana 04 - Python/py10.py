import os
from datetime import datetime

#print(dir(os))
print(os.getcwd()) #get current working directory
os.chdir('/home/murilo/Desktop')
print(os.getcwd())
print(os.listdir)

#os.mkdir("OS-Demo-2")
#os.mkdir("OS-Demo-2/Sub-Dir-1")
os.makedirs("OS-Demo-2/Sub-Dir-1")
os.removedirs('OS-Demo-2/Sub-Dir-1')
#os.rename('Controle Digital', 'CD')

#print(os.listdir)
#mod_time = os.stat('CD').st_mtime
#print(datetime.fromtimestamp(mod_time))

print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/home/murilo/Desktop/CD'))

print(dir(os.path))
