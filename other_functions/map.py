#map 함수는 데이터를 다룰 때 많이 사용

def two_times(x): return x*2

a = list(map(two_times,[1,2,3,4]))
print(a)

a = list(map(lambda a: a*2,[1,2,3,4]))
print(a)
