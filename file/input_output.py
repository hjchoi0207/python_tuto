f = open("new.txt",'w', encoding="UTF=8")
for i in range(1,11):
  data = ("%d번째 줄입니다.\n" % i)
  f.write(data)
f.close()

f = open("new.txt", "r", encoding="UTF-8")
while True:
  line = f.readline() # 한 줄만 읽어옴
  if not line: break
  print(line, end='')
f.close()

f = open("new.txt",'r', encoding = "UTF-8")
lines = f.readlines() #리스트 형태로 다 받아옴 
for i in lines:
  print(i.strip("\n"), end = ' ')
f.close()

f = open("new.txt", "r", encoding="UTF-8")
data = f.read() #그냥 다 가져옴
print(data)
f.close()
