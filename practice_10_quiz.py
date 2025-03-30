'''동네에 항상 대기 손님이 이는 맛있는 치킨집이 있습니다.
대기 손님의 치킨요리 시간을 줄이고자 자동주문 시스템을 제작하였습니다.
시스템코드를 확인하고 적절한 예외처리 구문을 넣으시오

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError 로 처리
        출력메시지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문 할 수 있는 총 치킨량은 10마리로 한정
        치킨소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력메시지 :  "재고가 소진되어 더 이상 주문을 받지 않습니다."'''

# # [코드] 내가 적은답
# class SoldOutError(Exception):
#     def __init__(self,msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg
    
# chicken = 10
# waiting = 1
# while(True):
#     try: 
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇마리 주문 하시겠습니까?"))
#         if order < 1:
#             raise ValueError
#         if order > chicken:
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 : {0}] {1}마리 주문이 완료되었습니다.".format(waiting,order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as e :
#         print(e)
#         break

#답 풀이

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try: 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문 하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 : {0}] {1}마리 주문이 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break