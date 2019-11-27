# 클래스 : 반복되는 불필요한 소스코드를 최소화하면서
#          현실세계의 사물을 컴퓨터프로그래밍 상에서
#          쉽게 표현할 수있게 해주는 프로그래밍 기술

# 인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용할 수있게 만든 변수
# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수 : 클래스 내부에 포함되는 함수, 메소드라고 부릅니다.

class Car:
    # 클래스의 생성자
    def __init__(self, name, color): # 매개변수 기본적으로 self
        self.name=name # 클래스의 멤버
        self.color=color # 클래스의 멤버
    # 클래스의 메소드
    def show_info(self):
        print("이름:", self.name,"색상:",self.color)
    # 클래스 소멸자
    def __del__(self):
         print("인스턴스를 소멸시킵니다.")
    # Setter 메소드
    def set_name(self, name):
            self.name = name

car1=Car("소나타","빨간색") # 자동차의 멤버를 입력
car1.show_info() # 자동차의 정보를 출력할 수있게한다.
print(car1.name,"을(를) 구매했습니다!") # 특정한 멤버변수에 접근가능
print("차량의 색은", car1.color,"입니다.")
del car1 # 한 번 사용하고 더이상 사용되지않는 객체를 할당해제합니다.

car2=Car("레이","민트색")
car2.set_name("벤츠") # 자동차의 멤버를 변경
car2.show_info()

# 상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
# 부모와 자식 관계가 존재합니다.
class Unit:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [전투력:",self.power,"]")

unit=Unit("나동빈", 999)
unit.attack()

class Monster(Unit): # Unit함수에 def attack~을 불러온다
    def __init__(self,name,power,type):
        self.name=name
        self.power=power
        self.type=type
    def show_info(self): # 자식클래스에서만 유효하다.
        print("몬스터 이름:",self.name,"/ 몬스터의 종류:",self.type)
monster=Monster("슬라임",10000,"초급")
monster.show_info()
monster.attack()