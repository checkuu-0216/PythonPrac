import random
#내가 푼 문제
people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
chiken = random.sample(people,1)
people.remove(chiken[0])
coffee = random.sample(people,3)
print(" --당첨자 발표-- ")
print("치킨 당첨자 : " + str(chiken))
print("커피 당첨자 : " + str(coffee))
print(" --축하합니다-- ")


# 셔플 쓰기 - 셔플해서 섞고 0번치킨주고 2에서4까지 커피주기
from random import *
people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(people)
chiken = people[0]
coffee = people[1:4]
print(" --당첨자 발표-- ")
print("치킨 당첨자 : " + str(chiken))
print("커피 당첨자 : " + str(coffee))
print(" --축하합니다-- ")

#다른답
users = range(1,21) # 1부터 20까지 숫자 생성
print(type(users))
users = list(users) #list로 변환하여 list에서 쓰는것들 쓰기
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(" --당첨자 발표-- ")
print("치킨 당첨자 : {0}" .format(str(winners[0]))) # format으로 넣어줄 값 넣어줬다.
print("커피 당첨자 : {0}" .format(str(winners[1:])))
print(" --축하합니다-- ")
