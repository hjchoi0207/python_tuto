
f = open('none.txt','w')
try:
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    f.close()

print('exec')   #실행된다
