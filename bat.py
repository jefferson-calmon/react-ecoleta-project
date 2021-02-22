import os
import time
import uuid

def commit():
    os.system('git add . > null')
    os.system('git commit -m "teste"')

def editFile(id):
    with open('README.md', 'a') as file:
        file.write(f'{str(id)} {uuid.uuid4()}')
        commit()

number = int(input('>>'))
ind = 0

while ind < number:
    editFile(ind)
    ind += 1
os.system('git push')
