#real garen damage

'''
This code will output at which point various targets would die based on the WHOLE Garen ultimate damage.
Taking into account both the base damage and the missing health damage

Display format:
Original HP the target had
The actual HP it had before being killable with the ultimate
The percentage of it's total hp it had before being killabe with the ultimate
'''

from math import floor

TD=[[150, 0.25], [300, 0.3], [450, 0.35]]

OV=700
#original/first victim

line= '_'*32+'\n'

for rank in range(3):
    print(f'{line*3}{"RANK "+str(rank+1):_^32}\n{line*3}')
    for i in range(67):
        ah=oh=OV+(50*i)
        while ah>=0:
            if ah-(TD[rank][0]+(oh-ah)*TD[rank][1])<=0:
                print(f'Original HP: {oh}\n'
                      f'Actual HP: {ah}\n'
                      f'Percentage: {floor((ah/oh)*100)}%HP\n'
                      f'{line}')
                break
            ah-=1

        

'''
pegar hp
mata? não ent
menos hp, mais missing h
matou?
reseta interação
'''

