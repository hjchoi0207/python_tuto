#Exception, 예외처리


'''
try:
    오류가 발생할 수 있는 구문을 실행하봄
except Exception as e:
    오류 발생했을 때 실행할 구문이며 except가 실행되어도 프로그램은 종료되지 않음
else:
    오류가 발생하지 않았을 때 실행할 구문
finally:
    항상 실행되며 마지막에 실행되는 구문
'''

try:
    4/0
except Exception as e:
    print(e)
print("exec")
