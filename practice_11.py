# #모듈

# # import theater_module

# # theater_module.price(3) # 3명일때 가격
# # theater_module.price_morning(4)
# # theater_module.price_soldier(5)

# # import theater_module as mv # 별명 짓기

# # mv.price(3)
# # mv.price_morning(4)
# # mv.price_morning(5)

# # from theater_module import * # theater_module 을 명시하지않고 바로 쓸수있음

# # price(3)
# # price_morning(4)
# # price_soldier(5)

# from theater_module import price, price_morning

# price(5)
# price_morning(5)
# # price_soldier(6) 쓸수없다

# from theater_module import price_soldier as price
# price(5)

# #패키지 - 모듈을 모아놓은 집합
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage 
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# # __all__
# from travel import *
# # # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # 패키지, 모듈 위치

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

#pip install