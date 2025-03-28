# # 함수 
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# #전달값과 반환 값
# def deposit(balance, money):
#     print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
#         return balance - money
#     else :
#         print("잔액이 부족하여 출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance , 1000)
# # balance = withdraw(balance, 500)
# commission , balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission,balance))

# #기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# #같은 학교 같은 학년 같은 수업듣는 상황
# def profile(name, age = 17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#           .format(name, age, main_lang))
    
# profile("유재석")
# profile("김태호")

# #키워드 값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#           .format(name, age, main_lang))
    
# profile(name = "유재석",age = 20,main_lang = "파이썬")
# profile(age = 20,main_lang = "파이썬",name = "김태호")

# #가변인자
# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end =" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end =" ")
#     for lang in language:
#       print(lang, end=" ")
#     print()

# profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
# profile("김태호",25,"Kotlin","Swift","","","")

# #지역변수 전역변수
# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun #전역공간에 있는 gun을 가지고 와서 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) #경계근무 나간 수
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
