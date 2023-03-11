# 01 Read from file
with open('input.txt') as f:
    lines = f.readlines()

# 02 Process data with algorithm
j = 0
k = 0
temp = 0
answer = 0
elves = []

for i in lines:
    j = j+1
    if i != "\n":
        temp = temp + int(i[:-1])
    else:
        elves.append(temp)
        k = k + 1
        temp = 0

# 03 Answer: obtain min of an array
elves.sort(reverse=True)
answer = elves[0]
print(answer)

answer = 0
j = 0
for i in elves:
    if j != 3:
        answer = answer + i
        j = j + 1
    else:
        break
print(answer)