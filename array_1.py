# Find the prime
# Find the duplicates
# delete value 10

#1:
values = [1,2,3,4,5,6,7,8,9,10,9,8,3,4,2]
for i in values:
    if i == 1:
        continue
    flag = 0
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            flag = 1
            print(i, 'Not Prime')
            break
    if flag == 0:
        print(i, 'Prime')

#2:
element = set()
duplicate = []
for i in values:
    if i not in element:
        element.add(i)
    else:
        duplicate.append(i)

print(duplicate)

#3:
val = 10
for i in range(len(values)):
    if values[i] == val:
        new = values[:i]+values[i+1:]
        break

print(new)