def factorial(n):
  ans = n
  for i in range(1,n):
    ans *= i

  return ans

for j in [2, 4, 10]:
  print(factorial(j))