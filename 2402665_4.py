# 과제 25
keys1 = input('alpha bravo charlie delta echo foxtrot golf 입력: ').split()
values1 = list(map(int, input('30 40 50 60 70 80 90 입력: ').split()))

my_dict1 = dict(zip(keys1, values1))
del my_dict1['alpha']
del my_dict1['delta']

print(my_dict1)

# 과제 26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83} 

print(park['english'], park['science'])

# 과제 27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83} 
x = dict.fromkeys(kim, 100)

print(x)

# 과제 28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83} 

if 'english' in lee:
    del lee['english']   

print(lee)

# 과제 29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83} 

for i, j in lim.items():
    print(i, j)

# 과제 30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83} 
choi = {key1: value1 for key1, value1 in choi.items() if value1 >= 90}

print(choi)

# 과제 31
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83} 
average = sum(yoo.values()) / len(yoo)

print(average)


