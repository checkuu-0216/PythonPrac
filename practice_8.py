# #표준 입출력
# print("Python" , "Java", "JavaScript", sep=",", end= "?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python" , "Java", file = sys.stdout)
# print("Python" , "Java", file = sys.stderr)

# #시험성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
# #     print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep =":") # 8칸확보후 왼쪽 정렬 , 4칸확보후 오른쪽 정렬

# #은행 대기 순번 표
# # 001, 002, 003 ...
# for num in range(1,41):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ") # 사용자 입력으로 받게되는 값은 항상 str 문자열로 타입이 지정된다.
# print("입력하신 값은 " + answer + "입니다.")

# #다양한 출력 포맷
# # 빈자리는 빈공간으로 두고 오른쪽 정렬을 하되 총 10자리 공간을 확보
# print("{0: >10}".format(500)) #오른쪽 정렬
# print("{0: <10}".format(500)) #왼쪽 정렬

# #양수일땐 + 로 표시, 음수일땐 -로 표시
# print("{0: >+10}".format(500)) # + 부호 없었을때도 -는 찍히나 양수일때는 숫자만 나옴
# print("{0: >+10}".format(-500)) 

# #왼쪽 정렬하고 빈칸을 _로 채움
# print("{0:_<+10}".format(500)) # 10칸 왼쪽정렬하고 나머지 _ _은 6칸
# #3자리마다 , 찍어주기
# print("{0:,}".format(10000000000))
# #3자리마다 , 찍고 +-부호도 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))
# #3자리마다 , 찍고 부호도 붙이고 자리수 확보
# # 빈자리는 ^로 채워보기
# print("{0:^<+30,}".format(10000000000))
# #소수점 출력
# print("{0:f}".format(5/3))
# #소수점 특정 자릿수까지 출력
# print("{0:.2f}".format(5/3))

# #파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 모든 라인들 가져와 list 형태로 저장
# for line in lines:
#     print(line, end ="")
# score_file.close()

# #pickle
# import pickle
# # profile_file = open("profile.pickle", "wb")
# # profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) #profile에 있는 정보를 profile file에 저장
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# #with
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","r", encoding="utf8") as study_file:
#     print(study_file.read())
