#exception을 여러개 만들 수 있다

try:
    4/0
    a=[1,2]
    print(a[3])
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다") #실행
except IndexError:
    pass #실행x, 실행되어도 그냥 지나감
