number = (int(input()))
password = []
for i in range(1, number // 2 +1):
    for j in range(i, number - i + 1):
        if number % (i + j) == 0 and j != i:
            password.append(str(i))
            password.append(str(j))
str = ''.join(password)
print(str)
