# 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱
jumin = "990325-1234567"

print("성별 : " + jumin[7] )
print("연 : " + jumin[0:2]) # 0 부터 2전까지 가져옴
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #뒷자리에서 몇번째앞까지 가져올때 - 붙히기

#문자열 처리함수
python = "Python is Amazing"
print(python)
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n" , index + 1)
print(index)

print(python.find("Java"))
# print(python.index("Java"))

print(python.count("n"))

#문자열 포맷
print("a"+ "b")
print("a" , "b")

print("나는 %d살 입니다." % 20) # %d 뒤에 적은 정수값을 넣어준다
print("나는 %s을 좋아해요" % '파이썬') # %s 뒤에 적은 스트링 값을 넣어준다
print("Apple 은 %c로 시작해요" % "A") # %c char 뒤에 한글자 값을 넣어준다
# %s로 하면 웬만하면 다 통한다.

print("나는 %s색과 %s색을 좋아해요" % ("파란" , "빨강")) # %뒤에 괄호를 넣고 적으면 순서대로 넣어서 출력된다.

print("나는 {}살 입니다.".format(20)) # {}를 사용하면 .format을 사용한다.
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨강")) #숫자를 지정해주면서 어떤 단어가 들어갈지 지정가능하다.
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20,color = "빨간")) #변수를 지정해서 넣어줄수 있다.

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") # f라고 쓴다음 "" 사용하면 앞서만든 변수를 사용가능하다.

#탈출문자
print("백문이 불여일견  \n 백견이 불여일타")
print("저는 '나도코딩' 입니다.")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")
print("저는 \'나도코딩\' 입니다.")
print(" C:\\Users\\pc\\Python313\\python.exe") # \\ 문장내에서는 \로 나온다
print("pine Apple\rred") #\r 커서를 맨앞으로 이동
print("Redd\b Apple") # \b 백스페이스 - 앞칸을 하나 지운다.
print("Red\tApple") # \t 탭을 사용한다.
