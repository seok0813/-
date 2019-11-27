# 딕셔너리 : 키와값 한 쌍을 원소로 가지는 자료형
dict={} # 중괄호
dict["안녕"]="Hello" # key값 [이내용]
dict["기적"]="Miracle"
dict["노력"]="efoort"
dict["안녕"]="Hi" # 변경

keys=dict.keys() # 키값만 출력하고 싶을때
print("키 :",keys)
key_list=list(keys) # 리스트형태로 바꿀 수있음
print("키 리스트 :", key_list)

values=dict.values() # 값만 출력하고 싶을 때
print("값 :", values)
value_list=list(values) # 리스트형태로 바꿀 수있음
print("값 리스트 :", value_list)

if "노력" in dict:
    print("[노력] 키가 존재합니다.")

del dict["기적"] # 삭제
dict.clear() # 모든원소 삭제
print(dict)
print("사전 자료형의 길이 :",len(dict)) # 삭제됐는지 확인

for i, k in enumerate(dict): #사전변수에 모든원소에 접근
# i = 인덱스, k = key값
    print("[인덱스 :",i,"] 한글 :", k,"/ 영어 :",dict[k])

scores={}
scores["윤준민"]=90
scores["박성제"]=85
scores["윤수빈"]=95
print(sorted(scores)) # 키로 정렬하기 (사전순서에 맞게)
print(sorted(scores, reverse=True)) # 키로 내림차순 정렬하기
print(sorted(scores.values())) # 값을 정렬하기 (위와동일)
