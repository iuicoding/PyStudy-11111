score = float(input("> 신우의 생일은?"))
if score == 4.11:
    print("정답")
if score != 4.11:
    print("너무해")


elif 4.11 < score:
    print("그래 난 일년내내 생일이야")


#6교시 수업내용
alist = [1, 2, 3, 4]

print(alist)

if 4 in alist:
    print("4 있어!!!")
if 111 not alist:
    print("먼개소리야")

print(alist[1])

alist = alist + [1]
alist = alist * 2
alist.append(8)
print(alist)

del alist[0]
alist.remove(2)
alist.pop(4)
alist.pop()
print(alist)

print(alist + [2])
print(alist * 3 )

for element in a:
    print(element)