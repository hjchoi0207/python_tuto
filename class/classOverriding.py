class FourCal:
    def __init__(self,first,second): #예약어 
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

#MoreFourCal의 부모 클래스느  FourCal
class MoreFourCal(FourCal):
    #클래스 추가
    def pow(self):
        result = self.first ** self.second
        return result
    #overriding
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result

a = MoreFourCal(4,2)
print(a.add()) # 기존 매서드 이용가능
print(a.pow()) # 새로운 매서드 추가
print(a.div()) # 기존 매서드 변경(상속에서의 오버라이딩)
