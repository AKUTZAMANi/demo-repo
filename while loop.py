 #1
i = 2
print(i, end=' ')
while i < 50:
  i += 3
  print(i, end=' ')
print()
#2
i = 100
print(i, end=' ')
while i > 0:
  i -= 1
  print(i, end=' ')
print()
#3
num = 0
total = 0
while num >= 0:
  num = eval(input('Enter a number (negative to stop): '))
  if num >= 0:
    total += num
print(total)
#4
num = 0
count = 0
total = 0
flag = False
while num != 5:
 num = eval(input('Enter a number (5 to stop): '))
 count += 1
 total += num
if num == 3:
  flag = True
print(count)
print(total)
if flag:
 print('Yes')
else:
 print('no')

#5
s = ''
while len(s) != 5:
  s = input('Enter a sttring of at least 5 characters: ')
 print(s[4])
#6
s = ''
while len(s) < 5:
  s = input('Enter a sttring of at least 5 characters: ')
i = -1
while i < 0 or i >= len(s):
  i = eval(input('enter an index into that string: '))
if i < 0 or i >= len(s):
 print('please enter a valid index.')
print(s[i])
#7
s ='a'
while s != '':
 s = input('enter a string: ')
 if s == s[::-1]:
  print('it\'s a palindrome')
 else:
  print('Not a palindrome')

#8
import random
num= eval(input('enter a number btw 20 and 100: '))
print(num, end=' ')
while num >= 0:
 num -= random.randint(1, 10)
 print(num, end=' ')
print()

#9
num = eval(input('enter a postive integer: '))
print(num, end=' ')
while num != 1:
 if num % 2 == 0:
  num = num // 2
 else:
  num = 3*num + 1
 print(num, end=' ')
print()

#10
L = []
count = 0
while count < 5:
    r = random.randint(1, 10)
    if r == 10:
        count += 1
    L.append(r)
print(L)

#11
L = [random.randint(1,5)]
for i in range(49):
    r = random.randint(1,5)
    while r == L[i]:
        r = random.randint(1, 5)
    L.append(r)
print(L)
#12
L = eval(input('enter a list: '))
i = 0
while i < len(L) and L[i] >= 0:
    i += 1
if i < len(L):
    L[i] = 0
print(L)

#13
L = eval(input('enter a list: '))
count = 0
i = 0
while count < 3 and i < len(L):
    while i< len(L) and L[i] >= 0:
        i += 1
        count += 1
        if i < len(L):
            L[i] = 0
print(L)
#14
s = input('enter a string with some letters and some letters and some non-letters: ')
i = 0
while i < len(s) and s[i].isalpha():
    i += 1
print(s[:i])
#15
import random
points = 100
while 0 < points < 200:
    r = random.randint(1,3)
    guess = eval(input(('your guess: ')))
    if guess < r:
        points -= 10
        print('too low.', end=' ')
    elif guess > r:
        points += 20
        print('too high.', end=' ')
    print('score:', points)
if points >= 200:
    print('you win!')
else:
    print('you lose')
#16
import random
guesses = 3
score = 0
while guesses > 0 and score < 200:
    x = random.randint(2, 99)
    y = random.randint(2, 99)
    print(x, 'x', y)
    ans = eval(input('your guess: '))
    if ans == x * y:
        score += x+y
        print('Score:', score, ' guesses left:', guesses)
if guesses == 0:
    print('you lose.')
else:
    print('you win!')

#17
import random
money = 50
turn = 10
guess = 1
while guess != 0 and money > 0 and turn >= 2:
    r = random.randint(1, turn)
    print('guessing from 1 to', turn)
    guess = eval(input('your guess: '))
    if guess == 0:
        print('you walk with this much: ', money)
    elif guess != r and 1 <= guess <= turn:
        money *= 2
        print('Computer guessed: ', r)
        print('you\'re still alive. you have this mmuch money: ', money)
        money = 0
    else:
        print('computer guessed:', r)
        print('Game over. You owe the computer this much: ',money)
        money = 0
if turn == 1:
    print('wow, you made it all the way through and earned this much: ', money)

#18
import random
s = input('enter a string with soe letters and some non-letters: ')
while True:
    indices = []
    for i in range(len(s)):
        if not s[i].isalpha():
            indices.append(i)
            if len(indices) == 0:
                break
            j = random.choice(indices)
            s = s[:j] + s[j+1:]
            print(s)
#19
n = eval(input('how many primes? '))
primes = []
p = 2
while n > 0:
    for i in range(2, p//2 + 1):
        if p % i == 0:
            break
    else:
        primes.append(p)
        n -= 1
    p += 1
print(primes)

#20
import random
n = eval(input('Entr n: '))
previous = []
i = 1
while True:
    r = random.randint(1, n)
    print(i, '. ', r, sep=' ')
    if r in previous:
        break
    previous.append(r)
    i += 1
#21
max_seq_len = 0
for i in range(10000):
    n = 0
    r = random.randint(1, 6)
    while r != 6:
        n += 1
        r = random.randint(1, 6)
    if n  > max_seq_len:
        max_seq_len = n
print(max_seq_len)


