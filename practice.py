# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# print( 5> 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 >10))

# 애완동물을 소개해 주세요!
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3
# print("우리집 "+ animal +"의 이름은 "+ name +"예요")
# # print(name +"는 "+str(age)+"살이며, "+ hobby +"을 아주 좋아해요")
# print(name, "는 ", age,"살이며, ", hobby, "을 아주 좋아해요")
# print(name +"는 어른일까요? " +str(is_adult))

##  Quiz) 변수를 이용하여 다음 문장을 출력하시오
##  변수명  : Station
##  변수값 :"사당", "신도림", "인천공항" 순서대로 입력
##  출력문장 : XX 행 열차가 들어오고 있습니다.
# Station ="사당"
# print(Station+"행 열차가 들어오고 있습니다.")
# Station ="신도림"
# print(Station+"행 열차가 들어오고 있습니다.")
# Station ="인천공항"
# print(Station+"행 열차가 들어오고 있습니다.")

# print(1+1) 
# print(3-2)
# print(5*2)
# print(6/3)
# print(2**3) #2^3=8
# print(5%3)  #나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 1
# print(10//3) # 3
# print(10>3)
# print(4>=7)
# print(10<3)
# print(5<=5)
# print(3==3)
# print(4==2)
# print(3+4==7)

# print(1 != 3)
# print(not(1 != 3))
# print((3>0) and (3<5))
# print((3>0)&(3<5))
# print((3>0) or (3>5))
# print((3>0)|(3>5))
# print(5>4>3)
# print(5>4>7)

# print(2+3*4)
# print((2+3)*4)
# number = 2+3*4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)
# number %= 5
# print(number)


# print(abs(-5)) #절대값
# print(pow(4, 2)) #제곱승
# print(max(5, 12)) #둘중 큰값
# print(min(5, 12)) #둘중 작은값
# print(round(3.14)) #반올림
# print(round(4.99)) #반올림

# from math import *
# print(floor(4.99)) #내림
# print(ceil(3.14)) #올림
# print(sqrt(16)) #제곱근

# from random import *
# print(random()) # 0.0 ~1.0 미만의 임의의 값 생성
# print(random() *10) # 0.0 ~10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~10 미만 정수의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~10 이하 정수의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하 정수의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하 정수의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하 정수의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하 정수의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하 정수의 임의의 값 생성
# print(int(random()*45)+1) # 1 ~ 45 이하 정수의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성
# print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~ 45 이하의 임의의 값 생성

## Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
## 월4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
## 아래의 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
## 조건1 : 랜덤으로 날짜를 뽑아야 함
## 조건2 :  월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
## 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
## (출력물 예제) 오프라인 스터디 모임 날짜는 매월 X일로 선정 되었습니다.
# from random import *
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 "+str(date) + "일로 선정 되었습니다.")

# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 =  """
# 나는 소년이고, 
# 파이썬이 쉬워요
# """
# print(sentence3)

# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0 부터 2 직전까지 (0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[0:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
# print(python.find("Java"))
# # print(python.index("Java")) #에러 발생
# print(python.count("n"))

##문자열 포맷
# print("a" + "b")
# print("a" , "b")
## 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")
## %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "삘간"))
## 방법 2
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "삘간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "삘간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "삘간"))
## 방법 3
# print("나는 {age}실이며 {color}색을 좋아해요." .format(age=20, color="빨간"))
# print("나는 {age}실이며 {color}색을 좋아해요." .format(color="빨간", age=20))
## 방법 4 (v3.6이상~)
# age=20
# color ="빨간"
# print(f"나는 {age}실이며 {color}색을 좋아해요.")

## 탈출문자
## \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")
## \" \' : 문장 내에서 따옴표
## 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")
## \\ : 문자 내에서 \
# print("D:\\PythonWorkspace")
## \r : 커서를 맨 앞으로 이동 그 이후 글짜 덮어쓰기
# print("Red Apple\rPine")
## \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")
## \t : 탭
# print("Red\tApple")

## 퀴즈3
##Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
##예) http://naver.com
## 규칙1 : http:// 부분은 제외 => naver.com
## 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
## 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
##                (nav)                 (5)          (1)             (!) 
## 예) 생성된 비밀번호 : nav51!
# site="http://naver.com"
# re_site = site.replace("http://","")
# re_site1 = re_site.index(".")
# re_site2 = re_site[0:re_site1]
# rule1 = re_site[0:3]
# rule2 = len(re_site2)
# rule3 = re_site.count("e")
# password = rule1+str(rule2)+str(rule3)+"!"
# print("{0}의 비밀번호는 {1}입니다".format(site,password))

## 리스트
## 지하철 칸별로 10명, 20명, 30명
## subway1 = 10
## subway2 = 20
## subway3 = 30
# subway = [10,20,30]
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# #조세호는 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
# #하하씨가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)
# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# # print(subway.pop())
# # print(subway)
# # print(subway.pop())
# # print(subway)
# # 같은 이름의 사람이 몇 명이 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
#정렬도 가능
# num_list = [5,4,3,2,1]
# num_list.sort()
# print(num_list)
# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)
# # 모두 지우기
# num_list.clear()
# print(num_list)
# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20,True]
# print(mix_list)
# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

## 사전
#사전의 내용처럼 해당하는 정보를 가져올 수 있음
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# # print(cabinet[5]) #값이 없으면 에러를 띄우고 프로그램을 종료해버린다.
# print(cabinet.get(5)) #값이 없으면 None으로 출력하고 뒤에 프로그램 실행함
# print(cabinet.get(5, "사용가능"))
# print("hi")
# print(3 in cabinet) # True
# print(5 in cabinet) # False
# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
# # 새손님
# print(cabinet)
# cabinet["A-3"]="김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)
# # 간손님
# del cabinet["A-3"]
# print(cabinet)
# # Key들만 출력
# print(cabinet.keys())
# # Value들만 출력
# print(cabinet.values())
# # Key, Value 쌍으로 출력
# print(cabinet.items())
# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

## 튜플 - 변경되지 않는 목록, 리스트보다 속도가 빠르다.
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# # menu.add("생선까스")  # 튜플은 add등 을 사용 할 수 없다.
# name = "김종국"
# age = 40
# hobby = "운동"
# print(name, age, hobby)
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

##세트 (집합, set)
# # 중복 안됨, 순서없음
# my_set = {1,2,3,3,3}
# print(my_set)
# java ={"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# # 교집합 (java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))
# # 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))
# # 차집합 (java를 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
# # java를 잊었어요
# java.remove("김태호")
# print(java)

## 자료구조의 변경
## 커피숍
# menu = {"커피", "우유","주스"}
# print(menu)
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))

# ## 퀴즈4
## Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
## 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
## 댓글 작성자들 중에 추첨을 통해 1명 치킨, 3명은 커피 쿠폰을 받게 됩니다.
## 추첨 프로그램을 작성하시오.
## 조건1 :  편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
## 조건2 :  댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가 
## 조건3 : random 모듈의 shuffle 과 sample을 활용
## (출력예제)
## -- 당청자 발표 --
## 치킨 당첨자 : 1
## 커피 당첨자 : [2,3,4]
## -- 축하합니다. --
## (활용 예제)
## from random import *
## lst = [1,2,3,4,5]
## print(lst)
## shuffle(lst)
## print(lst)
## print(sample(lst, 1))
# from random import *
# users = range(1,21)
# users = list(users)
# lucky = sample(users, 4)
# shuffle(lucky)
# print(" -- 당청자 발표 -- ")
# print("치킨 당첨자 : {0}" .format(lucky[0]))
# print("커피 당첨자 : {0}" .format(lucky[1:]))
# print(" -- 축하합니다 -- ")

##if
# weather = input("오늘 날씨는 어때요? ")
# if weather =="비" or weather =="눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼자" :
#     print("마스크를 챙기세요")
# else : 
#     print("준비물이 필요 없어요")
temp = int(input("기온은 어때요? "))
if 30 <= temp : 
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp  and temp <30 :
    print("괜찮은 날씨에요")
elif 0 <= temp <10 :
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")