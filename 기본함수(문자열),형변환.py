a="Hello_python"
'''
replace(원래값, 바꿀값)
count("") : 괄호안의 문자의 개수를 세어준다.
find("") : 괄호안의 문자의 인덱스위치
upper() : 대문자로 바꾸어준다.
lower() : 소문자로 바꾸어준다.
strip("") : 괄호안의 문자를 없애준다.
split(" ") : 괄호안의 문자를 기준으로 나누어 리스트를 만들어준다.
zfill(숫자) : 숫자만큼의 자리를 만들고 빈 자리는 0으로 채운다.
int() : 문자열을 숫자로 바꿔줌
'''
print(a.replace("Hello","Hi"))
print(a.count("l"))
print(a.find("py"))
print(a.upper())
print(a.lower())
print(a.strip("Hello"))
print(a.split("_"))

# 문자열인 숫자
b="9876"
print(b.zfill(5))
# 이건 왜 한줄로 안만들어질까?
c=int(b)
print(c+124)

# 형변환
# 실수형을 바꿈
print(float(3))
# 정수형으로 바꿈
print(int(3.0))
# 문자열로 바꿈
print(str(3))
# 문자열이 된게 맞는지 확인해보자
print(str(3)+"3")