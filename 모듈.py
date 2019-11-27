# 모듈 : 미리 작성된 함수 코드를 모아 놓은 파이썬 파일
import math
print(math.pow(3, 8)) # 제곱된 결과 3**8
print(math.sqrt(64)) # 제곱근
print(math.gcd(72, 24)) # 최대공약수

import 라이브러리 # 같은 프로젝트 폴더에있으면 사용가능
print(라이브러리.add(3, 7))
print(라이브러리.subtract(3, 7))

# 모듈파일이 큰 경우에, 하나의 함수만 사용하겠다고 설정가능
from 라이브러리 import add
print(add(3,7))

# 모듈파일 이름이 긴경우 짧게 사용할 수있다.
import 라이브러리 as t
print(t.add(3,7))