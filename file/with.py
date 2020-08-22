#f = open("new.txt",'w', encoding="UTF=8")
with open("new.txt", "w") as f:
  for i in range(1,11):
    data = ("%d번째 줄입니다.\n" % i)
    f.write(data)


with open("new.txt", "r") as f:
  data = f.read() 
  print(data)
