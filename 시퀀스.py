# 시퀀스(Sequence) : 문자열, 리스트, 튜플등의 인덱스를 가지는 자료형

string1="Hello World"
list=['H','e','l','l','o',' ','w','o','r','l','d']
tuple=['H','e','l','l','o',' ','w','o','r','l','d']
print(string1[0:5])
print(list[0:5])
print(tuple[0:5])

# 반복문 등에서 사용될 수있음
list1=[1,2,3,4,5]
print(5 in list1)
print(6 in list1)

if 3 in list1:
    print("3을 포함하고 있습니다.")

for i in list:
    print(i)
string2=", Python"
print(string1+string2)

# len(시퀀스 자료형) : 시퀀스 자료형의 길이를 출력하는 함수
print(len(string1+string2))