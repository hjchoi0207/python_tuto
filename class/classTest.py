class FourCal:
    def __init__(self,first,second): #예약어 
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal(1,2) #a는 self로 자동 대입
#a.setdata(1,2)
# a -> self
# 1 -> first
# 2 -> second
print(a.first)
print(a.second)
print(a.add())
