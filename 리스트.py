# 리스트 : 비슷한 성질을 가진 객체의 나열 (같은 자료형)
# 리스트안에 리스트를 넣을 수있구나~
# a는 차례로 학생들의 영어성적과 수학성적이다.
a=[
  [90, 85, 83, 40, 30, 20, 19, 48, 39, 59],
  [48, 53, 64, 76, 58, 34, 55, 85, 96, 85]
]
sum=0
english=a[0]
for i in english:
    sum=sum+i
# len() : 문자열의 길이(문자개수)값
print("영어평균점수:",sum/len(english))
sum=0
math=a[1]
for i in math :
    sum=sum+i
print("수학평균점수:",sum/len(math))

b = [1, 3, 5, 9, 7, 1]
'''
count(원소) : 리스트에서 특정 원소가 몇개 포함되어있는지
index(원소) : 리스트에서 특정 원소의 인덱스위치
'''
print(b.count(1))
print(b.index(3))
'''
append(원소) : 리스트의 뒤쪽에 새로운 원소를 삽입
sort() : 리스트를 오름차순으로 정렬
extend(리스트) : 리스트 뒤족에 다른 리스트를 삽입
insert(인덱스,원소) : 특정 위치에 원소를 삽입
remove(원소) : 리스트에서 특정 원소를 삭제
pop(인덱스) : 리스트에서 특정 인덱스를 삭제
reverse() : 리스트를 뒤집는다.
'''
b.append(9)
print(b)
b.sort()
print(b)
c=[4, 7, 9, 3]
b.extend(c)
print(b)
b.insert(3, 99) # 넣으면 뒤로 밀리는구나
print(b)
b.remove(1)
print(b) # 하나만 없어지는구나
b.pop(4)
print(b)
b.reverse()
print(b)