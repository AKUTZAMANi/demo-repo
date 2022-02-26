#1a

list=[]
for i in range(1,6):
    e= eval(input('Enter items: '))
    list.append(e)
print(list)
print('(a) no of items: ',len(list))
#1b
print('(b)',list[3])
print('(c)',list[-3:])
print('(d)',list[2:])
#e
print('(e)',list[::-1])
print('(f) large',max(list),'small', min(list))
print("(g) total no. of items: ",sum(list))
#h
if 0 in list:
    print('(h) first zero at: ',list.index(0))
else:
    print('(h) no zeroes in the list.')
list.sort()
print('(i) sorted: ',list)
del list[0]
print('(j) after deleting first item:',list)
list[-2]= 9876
print('(k) after changing second to last item:', list)
list.append(-500)
print('(l) after appending -500 to list:', list)

print("the index to 0: ", index)

#2
a= 100*[0]
print("list: ",a)
#3
L=[1,2,3,4,5]
copy = L
L[0] = 999
print('(a) copy=', copy)
#3b
L=[1,2,3,4,5]
copy = L[:]
L[0] = 999
print('(b) copy=', copy)
print(L)
#4
L=[]
for i in range(101):
    L.append(round((i**2),4))
print(L)
#5
import random
L=[]
for i in range(11):
    e= random.randint(1,20)
    L.append(e)
print(L)
#6
import random
L=[]
for i in range(20):
    e= random.randint(0,1)
    L.append(e)
print(L)
print("no. of zeroes", L.count(0))
#7
import random
L=[]
count = 0
for i in range(20):
    e= random.randint(1,1000)
    L.append(e)
    if e%2==0:
        count += 1
print(L)
print("no. of even no.:", count)
#8

L0= []
L=[]
for j in range(6):
    e= eval(input('enter no.: '))
    L0.append(e)
    if e>50:
        L.append(e)
print('L:',L0)
print('L0:',L)
#9
L=[]
for j in range(6):
    e= eval(input('enter no.: '))
    L.append(e)
print('smallest thing:',min(L), 'first index:',L[0])

#11
L=[]
for j in range(6):
    e= eval(input('enter no.: '))

    if e % 2 == 0:
        L.append(0)
    else:
        L.append(1)

print('list:', L)


#14
L=[]
for i in range(1,11):
    L += i*[i]

print(L)
#15
L=[]
L0=[]
L1=[]
for i in range(4):
    a = eval(input('enter no.: '))
    b = eval(input('enter no.: '))
    L.append(a)
    L0.append(b)
    if L[i] > L0[i]: #going element by element
        L1.append(L[i])
    else:
        L1.append(L0[i])

print(L)
print(L0)
print(L1)
#16
n = eval(input('how many triangular no. do you want?: '))
L=[]
total = 0
for i in range(1,n):
    total += i
    L.append(total)
print(L)
#17

L=[]
sums = []

for i in range(6):
    e= eval(input('enter no.: '))
    L.append(e)
    sums.append(sum(L[:i+1]))

    print(sums)
print()
#18
L = []
L0 = []
N = []
for i in range(4):
    e = eval(input('enter: '))
    f =eval(input('enter: '))
    L.append(e)
    L0.append(f)
    N.append(L[i])
    N.append(L0[i])
print(L)
print(L0)
print(N)

#19
L = []
save = L[0]
for i in range(6):
    e = eval(input('enter no.: '))
    L.append(e)

    L[i] = L[i+1]
    L[-1] = save
print(L)

