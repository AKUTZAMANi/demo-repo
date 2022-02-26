#1a
import random

L = []
for i in range(4):
    e = input('enter string: ')
    L.append(e)
print(L)
print('(a)',random.choice(L))
print('(b)',random.sample(L,3))
random.shuffle(L)
print('c)',L)

#2
import random

L= []
for i in range(100):

    L += random.choice('HT')

print(L)
#3
import random

L= 60*'A'+30*'B'+ 8*'C'+ 2*'D'
s = []
for i in range(1000):

    s += random.choice(L)

print(s)
#4
import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
n = eval(input('how long do you want password: '))
s = []
for i in range(n):
    s += random.choice(chars)
print(s)
print(s[:2])
print(s[3:])
#5
import random
verbs = ['went', 'took', 'walk', 'opens', 'sees', 'lifts', 'tries', 'smell', 'stand', 'push']
Nouns = ['dog', 'cheetah', 'panther', 'kaduna', 'stone', 'toy', 'house']
adjectives = ['old', 'new', 'dirty', 'shiny', 'red', 'cold', 'fake', 'happy', 'funny', 'heavy']
print('The', random.choice(adjectives), random.choice(Nouns), random.choice(verbs), 'the', random.choice(Nouns) + '.')

#6
import random
verbs = ['went', 'took', 'walk', 'opens', 'sees', 'lifts', 'tries', 'smell', 'stand', 'push']
Nouns = ['dog', 'cheetah', 'panther', 'kaduna', 'stone', 'toy', 'house']
adjectives = ['old', 'new', 'dirty', 'shiny', 'red', 'cold', 'fake', 'happy', 'funny', 'heavy']

N= random.sample(Nouns, 2)
print('The', random.choice(adjectives), N[0], random.choice(verbs), 'the', N[1] + '.')
#7
L = []
for suit in ['clubs', 'diamonds', 'hearts', 'spades']:
    for value in ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']:
        L.append(value +' of '+ suit)
random.shuffle(L)
print(L[:5])
print(L[1:-1])

#8
import random
s = input('enter a word: ')
indices = []
for i in range(len(s)):
    indices.append(i)
spots= random.sample(indices, 3)

t = ''
for i in range(len(s)):
    if i in spots:
        t += '*'
    else:
        t += s[i]
print(t)
#9
import random
s = input('enter a word: ')
indices = []
for i in range(len(s)):
    indices.append(i)
for i in range(len(s)):
    c = random.choice(indices)
    indices.remove(c)
    s = s[:c] + '*' + s[c+1:]
    print(s)
#10
L = []
indices = []
for i in range(21):
    L.append(i)
    indices.append(i-1)

for i in range(3):
    S = random.sample(indices,2)
    L[S[0]], L[S[1]] =L[S[1]], L[S[0]]
    #note a better way is this:
    # a, b = sample(indices)
    #L[a], L[b] = L[b], L[a]
print(L)
#11
s = input('enter bunch of words seperated by spaces: ')
print('A list of the individual words: ', s.split())
#12
L=[]
for i in range(4):
    s = input('Enter a list of emails as a list of strings: ')
    L.append(s)
print('Joined by semicolons: ', ';'.join(L))

#13
M =[]
s = input('enter a date in the the month/day/year format: ')
L = s.split('/')
print('month: ', L[0])
print('day: ', L[1])
print('year: ', L[2])
#14
s = input('enter a bunch of the word')
L = []
for word in s.split():
    L.append(word[0].upper() + word[1:])
print(' '.join(L))
#15
from itertools import permutations
for x in permutations('abcd'):
    print(''.join(x))
#16
s = input('enter several sentences ending with periods (with no period except at the end of sentences): ')
for sentence in s.split('.'):
    words = sentence.split(' ')
    print(words[-1])

#17
import math
L = [round(math.sqrt(i), 2) for i in range(1, 100)]
print('(a):', L)
#b
L = []
for i in range(4):
    s = eval(input('enter a list of integers: '))
    L.append(s)
M = [x+1 for x in L]
print('(b):', M)
#c
L = []
for i in range(4):
    s = eval(input('enter a list of integers: '))
    L.append(s)
M = [x for x in L if x%2==0]
print('(c):', M)

#d
L = eval(input('Enter a list of integers: '))
M = [max(x, 0) for x in L]
print('(d):', M)

#e
s = input('enter a string:')
L = [c for c in s if c.isalpha()]
print('(e):', L)

#f
L = eval(input('enter list of lists: '))
M = [S[-1] for S in L]
print('(f):', M)

#g
s = input('enter a string of lowercase letters: ')
L = [s.count(c) for c in 'abcdefghijklmnopqrstuvwxyz']
print('(g):', L)

#h
s = input('enter a string: ')
t =  input('enter another string of the same length: ')
L = [i for i in range(len(s)) if s[i] != t[i]]
print('(h):', L)

#18
L = eval(input('enter a list of test scores: '))
M = [[], [], [], [], []]
for x in L:
    if x>= 90:
        M[0].append(x)
    elif x >= 80:
        M[1].append(x)
    elif x >= 70:
        M[2].append(x)
    elif x >= 60:
        M[3].append(x)
    else:
        M[4].append(x)
print(M)
#19
import random
L = []
for i in range(6):
    M = []
    for j in range(6):
        M.append(random.randint(0,9))
    L.append(M)
#a
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()
#b
count = 0
for i in range(6):
    for j in range(6):
        if L[i][j] == 0:
            count += 1
print("no. of zeros: ",count)

#c
print(min(L[0]))
#d
print(max(L[j][4] for i in range(len(L))))

#e
print(sum(x for x in L[-1]))
#f
M = [L[i][j] for i in range(len(L)) for j in range(len(L[i]))]
print('f)',M)
#g
M = [[0]*len(L) for i in range(len(L))]
for i in range(len(L)):
    M[j][i] = L[i][j]
for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[j][i], end=' ')

#20
import random
L = [[random.randint(0,1) for j in range(10)] for i in range(10)]
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()
r = eval(input('enter row: '))
c = eval(input('enter column: '))

if L[r][c] == 1:
    print('Hit')
else:
    print('Miss!')

#21

L = [[random.randint(0,2) for j in range(6)] for i in range(6)]
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()

r1 = eval(input('enter starting row: '))
r2 = eval(input('enter ending row: '))
c1 = eval(input('enter starting column: '))
c2 = eval(input('enter ending column: '))

total = 0
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        total += L[i][j]
    print(total)

#22
L = [[random.randint(0,2) for j in range(15)] for i in range(15)]

for i in range(len(L)):
    for j in range(len(L[i])):
       print(L[i][j], end=' ')
    print()
total = 0
for i in range(len(L)):
    for j in range(i, len(L[i])):
        total += L[i][j]
print(total)
#23
L= [[random.randint(0,2) for j in range(15)] for i in range(15)]

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()
flag = False
# check horizontal
for i in range(len(L)):
    for j in range(1, len(L[i])):
        if L[i][j] == L[i-1][j] == 0:
            flag = True
# check vertical
for i in range(1, len(L)):
    for j in range(1, len(L[i])):
        if L[i][j-1] == L[i][j] == 0:
            flag = True
if flag:
    print('there are consecutive zeroes.')
else:
    print('No consecutive zeroes. ')

#24
n = eval(input('enter the size: '))
L = [[' ']*n for i in range(n)]
for i in range(n):
    L[0][i] = L[-1][i] = L[i][0] = L[i][-1] = L[i][i] = L[i][n-i-1] ='#'
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()
#25










