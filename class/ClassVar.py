class FourCal:
    #클래스변수 선언
    first = 2
    second = 3
    #def __init__(self,first,second): #예약어, 객체변수 정의
    #    self.first = first
    #    self.second = second

a = FourCal()
print(a.first)
b = FourCal()
b.first = 20 #클래스변수는 호출 후 변경이 가능하다
print(b.first)
