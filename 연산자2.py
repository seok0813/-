# 증감 연산자 : 기존에 사용하던 증감 기능을 짧게 이용
# C언어에서의 증감 연산자 : ++, --가있는데 파이썬에서 사용X
# 축약형 => 증감 연산자
a = 10
a += 10
print(a)
# 관계 연산자 : 두 개의 값을 비교하여 관계
# A == B : A가 B와 같은지 판별 => True, False
# A != B : A가 B와 다른지 판별 => True, False
# A > B : A가 B보다 큰지 판별
# A < B : A가 B보다 작은지 판별
a=3
b=7
print(a==b) # F
print(a!=b) # T
print(a>b) # F

a="ABC"
b="DEF"
print(a==b)
print(a<b) # 문자열의 비교는 사전순으로 비교한다.

# 논리 연산자 : 여러 개의 수식을 논리적으로 연산
# A and B : A와 B가 모두 참인지 판별
# A or B : A혹은 B가 참인지 판별
# not A : A가 거짓인지 판별
a=True
b=False
print(a and b) # F
print(a or b) # T
print(not a) # F

if 3>5 or 7<10: # if True:
    print("야호!")