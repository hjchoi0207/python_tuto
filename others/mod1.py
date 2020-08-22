#mod1.py

def add(a,b):
    return a + b


#다른 프로그램에 import 하지않고 mod1만 사용시 실행됨
if __name__ == "__main__":
    print(add(10,20))
    print(add(30,40))
