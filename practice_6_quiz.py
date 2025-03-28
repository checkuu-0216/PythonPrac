from random import *

# #문제를 보고 내가 푼 정답 
# customer = range(1,51)
# time = int(random()*50) + 5
# index = 1

# while True:
#     if time <= 15:
#         print("{0} 번째 손님 (소요시간 : {1})".format(customer,time))
#         index += 1
#     elif time > 15:
#         continue
#     else:
#         break

# print("총 탑승 승객 : {0} 분".format(index))

cnt = 0 #총 탑승 승객 수
for i in range(1,51): # 1~ 50 이라는 승객 수
    time = randrange(5, 51) # 5분에서 50분 소요시간
    if 5<= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {0} 분".format(cnt))