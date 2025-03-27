
import random

# online1 = randint(4,28)
# online2 = randint(4,28)
# online3 = randint(4,28)
# offline = randint(4,28)

# print("월별 스터디 모임 날짜는 온라인 매월 " + str(online1) +" , "+ str(online2) +" , "+ str(online3) + "일로 선정되었습니다. 오프라인은 매월 " + str(offline) + "일로 선정되었습니다.")

date = random.sample(range(4,29) ,4)
date[:3] = sorted(date[:3])

print("월별 스터디 모임 날짜는 온라인 매월 " + str(date[0]) +" , "+ str(date[1]) +" , "+ str(date[2]) + "일로 선정되었습니다. 오프라인은 매월 " + str(date[3]) + "일로 선정되었습니다.")


date = random.sample(range(1, 46), 6)  # 1부터 45까지의 숫자 중 6개 뽑기
date.sort()  # 오름차순 정렬

# str()을 사용해 숫자를 문자열로 변환
print("이번주 로또 번호는 " + str(date[0]) + " , " + str(date[1]) + " , " + str(date[2]) + " , " + str(date[3]) + " , " + str(date[4]) + " , " + str(date[5]) + " 입니다.")