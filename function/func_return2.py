def sum_and_mul(a,b):
  return a+b,a*b

print(sum_and_mul(10,20))    #tuple(30, 200)
print(sum_and_mul(10,20)[0]) #30
print(sum_and_mul(10,20)[1]) #200
print(sum_and_mul(10,20)[2]) # error 
