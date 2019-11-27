# 튜플(Tuple) : 리스트와 비슷한 자료형 (변경 불가)
tuple=(1,2,3)
print(tuple)

for i in tuple:
    print(i)

list1=[1,2,3]
list2=[4,5,6]
tuple=(list1,list2)
print(tuple[0][1]) # 신기하네 tuple[0][1] => list1의 인덱스 1
print(tuple[1][1])

#튜플의 원소자체는 바꿀수없지만, 원소로 리스트가 있을경우 바꿀수있다.
tuple[0][1]=7
print(tuple)

# 인덱싱, 슬라이싱등의 문법도 그대로 사용 가능
tuple=(1,2,3,4,5,6,7,8)
print(tuple[0:5]*3) # 곱셈도 되네