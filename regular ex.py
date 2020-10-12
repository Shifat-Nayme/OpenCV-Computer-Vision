import re
nameage = '''
Shifat is 23 Fuad is 21
Sakib is 20 Janice is 22'''
ages = re.findall(r'\d{2}', nameage)
names = re.findall(r'[A-Z][a-z]*',nameage)
agedict ={}
x =0
for eachname in names:
     agedict[eachname] = ages[x]
     x+=1

print(agedict)
