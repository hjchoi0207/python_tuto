# *args 인자를 통해 여러 인자를 입력받을 수 있음
def sum_many(*args):
  sum =0
  for i in args:
    sum += i
  return sum

print(sum_many(1,2,3))
