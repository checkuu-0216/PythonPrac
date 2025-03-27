# #리스트

# #지하철 칸별로 10명 20명 30명

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇번째 칸에 타고있는가?
# print(subway.index("조세호")+1)

# #하하씨가 다음정류장에 탔다
# subway.append("하하")
# print(subway)

# #정형돈씨를 중간에 넣기
# subway.insert(1,"정형돈")
# print(subway)

# # 지하철에 있는 사람을 한명씩 꺼냄
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇명있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬도 가능
# num_list = [ 5,4,2,3,1]
# num_list.sort()
# print(num_list)
# #순서 뒤집기
# num_list.reverse()
# print(num_list)
# #모두 지우기
# num_list.clear()
# print(num_list)

# #다양한 자료형 함께 사용 가능
# mix_list = ["조세호", 20 , False]
# num_list = [ 5,4,2,3,1]
# # print(mix_list)

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#사전
# cabinet = {"a-3":"유재석", "b-100":"김태호"}
# print(cabinet[100])
# print(cabinet.get(3))
# # print(cabinet[5]) 일반 키를 넣으면 에러뜨면서 종료되나 .get을 이용하면 없을시 none이뜨고 작동한다.
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능")) # none 일때 뒤에 적은 값이 나온다.

# print(3 in cabinet)
# print(5 in cabinet)

# print(cabinet["a-3"])
# print(cabinet.get("a-3"))

# cabinet["c-20"] = "조세호"
# print(cabinet)

# cabinet["a-3"] = "김종국"
# cabinet["c-20"] = "조세호"
# print(cabinet)

# del cabinet["a-3"]
# print(cabinet)

# print(cabinet.keys()) # key 값만 알려줌
# print(cabinet.values()) # value 값만 알려줌
# print(cabinet.items()) # 쌍으로 출력력

# cabinet.clear() # 내용 지우기기
# print(cabinet)

#튜플
#내용 변경은 어려우나 list 보다 빠름
# menu = ("돈까스" , "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") 이런 추가가 안됨

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name,age,hobby)

# (name , age , hobby) = ("김종국" , 20 , "코딩")
# print(name ,age ,hobby)

# #세트
# #중복이 안되고 순서가 없음
# my_set = {1,2,3,3,4}
# print(my_set)

# java = {"유재석" , "김태호" , "양세형"}
# python = set(["유재석" , "박명수"])
# #교집합
# print(java & python)
# print(java.intersection(python))
# #합집합
# print(java | python)
# print(java.union(python))
# #차집합
# print(java - python)
# print(java.difference(python))
# #python 할줄아는 사람이 늘어남
# python.add("김태호")
# print(python)
# #java를 까먹음
# java.remove("김태호")
# print(java)

# #자료구조 변경
# menu = {"커피" , "우유" , "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu,type(menu))

# menu = set(menu)
# print(menu, type(menu))