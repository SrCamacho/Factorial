def factorial(n):
  ans = n
  for i in range(1,n):
    ans *= i

  return ans

print(factorial(5))