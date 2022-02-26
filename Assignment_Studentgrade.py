size = 8
for i in range(size):
    print ('* ' * size)


#########################
m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [0, n-3] or j in [0, m-2] else ' ', end='')
    print()
###########################
m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [j, m-1] or j == 0 else ' ', end='')
    print()

###########################
print("Enter width")
width = int(input())
print("Enter height")
height = int(input())

for i in range(height):
    if i in[0]:
        print("* "*(width))
    elif i in[(height-1)]:
        print("* "*(width))
    else:
        print("*"+"  "*(width-2)+" *")

input()
