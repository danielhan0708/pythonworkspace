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
# users = range(1,21) # 1부터 20까지 숫자를 생성
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
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else : 
#     print("준비물이 필요 없어요")
# temp = int(input("기온은 어때요? "))
# if 30 <= temp : 
#     print("너무 더워요. 나가지 마세요.")
# elif 10 <= temp  and temp <30 :
#     print("괜찮은 날씨에요")
# elif 0 <= temp <10 :
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

## for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# #randrange()
# for waiting_no in range(1, 6): # 1,2,3,4,5
#     print("대기번호 : {0}" .format(waiting_no))
# starbucks = ["아이언맨", "토르", "캡틴 아메리카"]
# for customer in starbucks:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))

## while
# customer = "토르"
# index =  5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았습니다." .format(customer, index))
#     index -=1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회" .format(customer, index))
#     index += 1
# customer = "토르"
# person = "Unknown"
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ") 

## continue 와 break
# absent = [2,5] #결석
# no_book =[7]
# for student in range(1, 11) : #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

## 한줄 for
# #출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 --> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)
# #학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "Captin America"]
# students = [len(i) for i in students]
# print(students)
# #학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "Captin America"]
# students = [i.upper() for i in students]
# print(students)

## 퀴즈 5
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건1 :  승객별 운행 소요 시간은 5분 ~ 50분 사이의 승객만 매칭해야 합니다.
# 조건2 :  당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# (출력물 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2분
# 풀이
# from random import *
# mywork_time = range(5,15)                  #5분~ 15분 소요 시간
# cnt = 0                                    #총 탑승 승객 수
# for customers in range(1,51):              #1 ~ 50 승객 수
#     arrive_time = randint(5,50)            #5분 ~ 50분 소요시간
#     if arrive_time in mywork_time :        #5분 ~ 15분 이내의 손님(매칭성공)
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customers, arrive_time))
#         cnt += 1                           #탑승 승객 수 증가 처리
#     else :                                 #매칭 실패
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customers, arrive_time))
# print("총 탑승 승객 : {0} 분".format(cnt))

## 함수 
# def open_account():
#     print("새로운 계좌가 생성 되었습니다.")
# open_account()

##전달 값과 반환 값
# def deposit(balance, money): #입금
#     print("입금이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
#     return balance + money
# def withdraw(balance, money): #출금
#     if balance >= money: #잔액이 출금보다 많으면
#         print("출금이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
# def withdraw_night(balance, money): #영업외 시간에 출금
#     commission = 100 #수수료 100원
#     print("수수료는 {0} 원이며 잔액은 {1} 원입니다.".format(commission, balance))
#     return commission, balance - money - commission
# balance =  0 #잔액
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)

## 기본값
# def profile(name, age, main_lang):
#     print("이름 :  {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
# # #같은 학교 같은 학년 같은 반 같은 수업
# def profile1(name, age=17, main_lang="파이썬"):
#     print("이름 :  {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang))
# profile1("유재석")
# profile1("김태호")

##키워드 값
# def profile(name, age, main_lang):
#      print("이름 :  {0}\t나이 : {1}\t주 사용 언어: {2}" \
#          .format(name, age, main_lang))
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

##가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
# def profile(name, age, *langauge):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in langauge:
#         print(lang, end=" ")
#     print()
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")

##지역변수와 전역변수
# gun = 10
# def checkpoint(soldiers): #경계근무
#     global gun #전역 공간에 있는 gun을 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계 근무
# print("남은 총 : {0}".format(gun))
# def checkpoint_ret(gun, soldiers): #경계근무
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2) #2명이 경계 근무
# print("남은 총 : {0}".format(gun))

# ##퀴즈 6
# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
# #풀이
# height =  175
# gender = '남자'
# def std_weight(height, gender):
#     if gender == '남자' :
#         return height * height * 22
#     elif gender == '여자' :
#         return height * height * 21
#     else :
#         print("잘못된 입력입니다.")
# weight = round(std_weight(height/100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

##표준 입출력 
# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")
# import sys
# print("Pyton", "Java", file=sys.stdout) #표준 출력
# print("Pyton", "Java", file=sys.stderr) #표준 에러처리
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
#     # print(suject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
# 은행 대기순번표
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")

## 다양한 출력 포맷
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000000))
# # 3자리 마다 콤마를 찍어주기,  +- 부호도 붙이기
# print("{0:+,}".format(100000000000000))
# print("{0:+,}".format(-100000000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채우기
# print("{0:^<+30,}".format(100000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

## 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") #파일에 쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# score_file = open("score.txt", "a", encoding="utf8") #파일에 이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8") #파일 읽어오기
# print(score_file.read()) #전체읽기
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8") #파일 읽어오기
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8") #파일 읽어오기
# while True:                                         #파일의 줄 갯수를 모를 때 반복문으로 처리
#     line =  score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8") #파일 읽어오기
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file. close()

##pickle
# import pickle
# profile_file = open("profile.pickle", "wb") #피클 바이너리 형태로 해야 함
# profile = {"이름":"박명수", "나이":30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()
# profile_file = open("profile.pickle", "rb") #피클 바이너리 형태로 해야 함
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

##with
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

# ## 퀴즈7
# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무요약 :
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 :  파일명은  '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
## 3:33:35
# for week in range(1, 51):
#     with open("{0}주차.txt".format(week), "w",encoding="utf-8") as report_file:
#         report_file.write(" - {0} 주차 주간 보고 -".format(week))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무요약 : ")

# ## Class , __init__, 멤버변수
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40       # 유닛의 체력
# damage = 5    # 유닛의 공격력
# print("{} 유닛이 생성 되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
# # 탱크 : 공격 유닛, 탱크. 포을 쏠 수 있음, 일반모드 / 시즈모드
# tank_name = "탱크" # 유닛의 이름
# tank_hp = 150       # 유닛의 체력
# tank_damage = 35    # 유닛의 공격력
# print("{} 유닛이 생성 되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 :  {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

## 메소드, 상속
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(self.name, location, self.speed))
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0} : {1}데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은  {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
# #파이어뱃 : 공격 유닛, 화염 방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

## 다중상속 (상속에 이어서)
# 드라쉽 : 공중 유닛, 수송기. 공격X
# 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_seed = flying_speed
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_seed))
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 유닛의 speed 0으로 처리
#         Flyable.__init__(self, flying_speed)
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
# 발키리 : 공중공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시") 

## 연산자 오버로딩        
# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)
# # 배틀크루져 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

## Pass
# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #pass
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location
# #서플라이 디폿 : 건물, 1개 건물 = 8 유닛 생산.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     pass     
# game_start()
# game_over()

##super
# class Unit_1:
#     def __init__(self):
#         print("Uint 생성자")
# class Flyable_1:
#     def __init__(self):
#         print("Flyable 생성자")
# class FlyableUnit_1(Unit_1, Flyable_1):
#     def __init__(self):
#         # super().__init__()
#         Unit_1.__init__(self)
#         Flyable_1.__init__(self)
# #드라쉽
# dropship = FlyableUnit_1()

## 퀴즈 8
# #Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# #(출력예제)
# #총 3대의 매물이 있습니다.
# #강남 아파트 매매 10억 2010년
# #마포 오피스텔 전세 5억 2007년
# #송파 빌라 월세 500/50 2000년
# #[코드]
# class House:
#     #매물 초기화
#     def __init__(self, locaion, house_type, deal_type, price, completion_year):
#         self.location = locaion
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#     #매물 정보 표시
#     def show_detail(self):
#         print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
# h1 = House("강남","아파트","매매","10억","2010년")
# h2 = House("마포","오피스텔","전세","5억","2007년")
# h3 = House("송파","빌라","월세","500/50","2000년")
# houses =[]
# houses.append(h1)
# houses.append(h2)
# houses.append(h3)
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for unit in houses:
#     unit.show_detail()
    
 ## 예외처리   
# try: 
#     print("나누기 전용 계산기 입니다.")
#     # num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     # num2 = int(input("두 번째 숫자를 입력하세요 : "))    
#     # print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
#     nums =[]
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))    
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알수 없는 에러가 잘생하였습니다.")
#     print(err)

## 에러 만들기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

## 사용자 정의 예외처리 , finally
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

## 퀴즈 9
# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 디자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.
# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생 시키고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
# [코드]
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order < 1 :
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#             if chicken == 0:
#                 raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as err:
#         print(err)
#         break

## 모듈
# import thrater_module
# thrater_module.price(3) #3명이서 영화 보러 갔을 때 가격
# thrater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# thrater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때
# import thrater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)
# from thrater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)
# from thrater_module import price, price_morning
# price(5)
# price_morning(6)
# from thrater_module import price_soldier as ps
# ps(5)

## 패키지
# import travel.thailand
# trip_to = travel.thailand.TailandPackage()
# trip_to.detail()
# from travel.thailand import TailandPackage
# trip_to = TailandPackage()
# trip_to.detail()
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

## __all__ , 모듈 직접 실행
# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.TailandPackage()
# trip_to.detail()

##  패키지, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))
# from travel import *
# print(inspect.getfile(thailand))

## pip install
## https://pypi.org/project/beautifulsoup4/
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

## 내장함수
# #input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.".format(language))
# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random #외장함수
# print(dir())
# import pickle
# print(dir())
# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))
# name ="Jim"
# print(dir(name))
##https://docs.python.org/ko/3/library/functions.html

## 외장함수
##https://docs.python.org/ko/3/py-modindex.html
# # glob : 경로 내에 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))
# # os : 운영체제에서 제공하는 기본 기능
# import os
# print((os.getcwd())) # 현재 디렉토리
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os,os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print((os.listdir))
# # time
# import time
# print(time.localtime())
# print(time.strftime("%y-%m-%d %H:%M:%S"))
# import datetime
# print("오늘날짜는 ", datetime.date.today())
# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은 ", today + td) # 오늘부터 100일 후

## 퀴즈 10
# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건 : 모듈 파일명은 byme.py 로 저장
# (모듈 사용 예제)
# import byme
# byme.sign()
# (출력 예제)
# 이 프로그램은 다니엘에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : d.s.han0708@gmail.com
# with open("byme.py", "w",encoding="utf-8") as report_file:
#         report_file.write("def sign():")
#         report_file.write("\n    print(\"이 프로그램은 다니엘에 의해 만들어졌습니다.\")")
#         report_file.write("\n    print(\"유튜브 : http://youtube.com\")")
#         report_file.write("\n    print(\"이메일 : d.s.han0708@gmail.com\")")
# import byme
# byme.sign()
