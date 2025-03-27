# 내가푼 정답답
ex = "http://google.com"
# print(ex[7:])
ex = ex[7:]
# print(ex[:-4])
ex = ex[:-4]
print("생성된 비밀번호 : " + str(ex[:3]) + str(len(ex)) + str(ex.count("e")) +"!")

#정답답
url = "http://google.com"
url1 = url.replace("http://" , "")
url2 = url1[:url1.index(".")]
# print(url2)
password = url2[:3] + str(len(url2)) + str(url2.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url,password))
