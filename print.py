# 파이썬에서 print안에 띄어쓰기는 \n바로 붙여 넣거나 아니면 '''or"""바로이용

print('''\
    *
    **
    ***
    ****
    *****
    ''')

#6
print("\"!@#$%^&*()\'")

#7
print("\"C:\\Download\\\'hello\'.py\"")
print('"C:\Download\hello.cpp"')


#8
print('print("Hello\\nWorld")')

#9
a = input()
print(a)

#10
a = input() # a = int(input())로 한 번에 가능
a = int(a)
print(a)

#11
f = input()
f = float(f)
print(f)

#12
a = int(input())
b = int(input())
print(a)
print(b)

#13
a = input()
b = input()
print(b)
print(a)

#14
f = input()
print(f)
print(f)
print(f)

#15
a, b = input().split() # 이건 파이썬에서만 된다.
print(a)
print(b)

#15_2
var = list(map(int, input().split(' '))) #int형으로 캐스팅을 해야해서 map을 씀. map은 iterable(tuple, list 등)에 사용. 그리고 이걸 map 형태로 저장되기에 list로 다시 캐스팅
print( *var ) # *이용하면 전체 내용을 포인터처럼 받아오고,
print(var[0], var[1]) #이렇게 개별로도 받아올 수 있다.