#garen true damage

#This code will output the point at which a range of victims would die based solely on their missing HP
#Made to give myself some notion about it.

from math import ceil

victimsHP=[700,900,950,1000,1200,1400,1800,2000,2500,3000,4000,5000]

TD=[0.25,0.30,0.35]         #percentage of missing health as true damage

for originalHP in victimsHP:
    print(f'\n\n\n{originalHP} health champ:')
    HP=originalHP
    for level in range(3):
        losthealth=0
        while HP>0:
            if HP-(TD[level]*losthealth)<=0:
                #print(f'{originalHP} Health champion has died on {HP} HP, {losthealth} missing health')
                print(f'level {level+1}: {HP} HP\n'
                      f'Kill: {ceil((HP/originalHP)*100)}% HP\n\n')
                break
            HP-=1
            losthealth+=1
        HP=originalHP
        
