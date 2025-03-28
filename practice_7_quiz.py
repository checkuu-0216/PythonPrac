'''표준 체중을 구하는 프로그램 작성
표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키 (m) x 22
여자 : 키(m) x 키 (m) x 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        함수명 : std_weight
        전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시'''

# #내가 작성한 답
# gender = input("성별을 입력해 주세요 (여성, 남성) : ")
# height = int(input("키를 입력해 주세요 : "))


# def std_weight (gender , height):
#     if gender == "여성":
#         weight = (height/100) * (height/100) * 21
#     else:
#         weight = (height/100) * (height/100) * 22
#     return round(weight,2)

# print("표준 체중은 {0}kg 입니다.".format(str(std_weight(gender , height))))

# #다른 답
# def std_weight (height ,gender ):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
    
# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100,gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))