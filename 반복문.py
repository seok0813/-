# #예약어=>어떠한 목적으로 예약이 됨, 즉 변수명으로 지정할 수없다.
import keyword
print(keyword.kwlist)
# 반복문: 조건에 부합하는 한 특정한 명령어를 반복
# 숫자범위표현 : range(시작, 끝)
# 이거 왜 1~9까지 뜨냐...? 끝-1까지 뺀거까지 반복한다고 한다.
sum=0
for i in range(1,10):
    print(i)
#항상 sum=sum+i 할땐 앞에 sum=0 해줘야하나봄
    sum=sum+i
print("합계:", sum)
count=0
# 각 문자를 하나씩 방문?함
for i in "Hello World":
    if i=='o':
        count=count+1
print("o의 개수는", count,"개 입니다.")
#리스트
sum=0
list=[1, 2, 3, 4, 5]
for i in list:
    sum=sum+i
print("합계:", sum)
''' continue: continue를 만났을 때 더 이상 명령어를 실행하지 않고 다음 반복을 진행합니다. (한번의 반복을 건너 뛸 때)
    break: break를 만나면 반복문을 벗어납니다.
'''
# 1부터5까지 하나씩 확인하면서 짝수일때만 더하는 프로그램
# %가 나머지를 구하는 연산자를 통해 홀/짝을 표현할 수있음
sum=0
list=[1,2,3,4,5]
for i in list:
    if i%2==1 :
        continue
    sum=sum+i
    print("합계:",sum)
# while문 : 특정한 조건을 만족할 때만 계속해서 소스코드를 반복
i=0
sum=0
while i<5:
# i=i+1면 5까지 범위안에 넣었을 때 5+1=6까지 출력이 된다.
    i=i+1
    if i%2==1:
        continue
    sum=sum+i
print("합계:",sum)
