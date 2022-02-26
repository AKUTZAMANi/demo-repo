#1
lines = [line.strip() for line in open('expenses.txt')]
for item in lines:
    if int(item)> 2000:
        print(item, end=' ')
print()
