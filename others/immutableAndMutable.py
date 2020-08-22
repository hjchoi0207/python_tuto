#정수 실수 문자열 튜플
a = 1
def vartest(a):
    a = a + 1 #지역변수이며 값을 전달받아 연산

vartest(a)
print(a)


######################
#리스트 딕셔너리 집합#
b = [1,2,3]
def vartest2(b):
    b = b.append(4) #지역변수지만 같은 주소를 가

vartest2(b)
print(b)
  
