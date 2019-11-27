# 함수 : 특정한 입력을 받아서 처리를 한 후에 특정한 출력을 하는 모듈
# 함수를 이용하면 특정한 소스코드의 반복을 줄일 수있다.
def add(a, b): # def 함수이름(매개변수):
    sum = a+b  # 처리
    return sum # 출력 add(a,b)를 sum으로 바꿔준다는 의미 (없어도됨)
print(add(1,2))

def add(a, b):
    print(a+b)
add(1,2)

# 가변 인자 : 함수의 매개변수가 가변적일 수 있을 때 사용
def function(*data): # 매개변수가 몇개인지 모를 때
    print(data)      # 튜플형태로 처리됨
function(1,2,3)

# 전역 변수 : 소스코드 전체 어디에서든지 사용가능한 변수
# 지역 변수 : 특정한 함수(블록) 안에서만 사용할 수있는 변수
def add(a):
    a=a+5 # 지역 변수 : 함수가 종료되면 더 이상 사용되지않음
          # add() : \n global a : 전역변수로 사용가능

a=2 # 전역 변수
add(a)
print(a) # 2가 출력

# 파이썬의 함수는 반환 값이 여러 개일 수있음
def function():
    a=5
    b=[1,2,3]
    return a,b

a,b = function()
print(a)
print(b)