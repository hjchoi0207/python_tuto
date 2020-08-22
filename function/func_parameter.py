def say_myself(name, old, man=True):
  print("이름 :",name)
  print("나이 :",old)
  if man:
    print("남자입니다\n")
  else:
    print("여자입니다\n")
  
say_myself('John',25,True)
say_myself('james',26)
say_myself('anni',20,False)
