'''
조건문등에서 들여쓰기가 사용되는 규칙
첫 명령어는 들여쓰기 없이 시작해야한다.
조건문, 반복문 등의 문법을 사용할 때 콜론: 으로 명령어의 끝을 알려아한다.
콜론의 다음 줄부터는 들여쓰기의 간격이 모두 일정해야한다.
'''


score = 1
if score >=90 :
    print("Perfect\n말이 필요없네요. 훌륭합니다.")
elif score < 90 and score >= 80 : # and, or 수학처럼 90>s>80 이렇게하면 식마다 구분해야하기때문에 에러남
    print("Excellent\n와 제법이네요.")
elif score >= 70:
    print("Not Bad\n사람구실은 하겠네요.")
elif score == 0:
    print("쓰레기네요.")
else:
    print("Bad")
print("츄라이츄라이")

list=[1,3]
if 2 in list:
    print("2가 리스트에 포함되어 있습니다.")
else:
    print("2가 리스트에 포함되어 있지않습니다.")