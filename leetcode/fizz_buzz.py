# fizz_buzz.py
class Solution:
    def fizzBuzz(self, n):
        result = []

        for i in range(1, n+1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result 

n = 15 
sol = Solution()
print(n)
print(sol.fizzBuzz(n))
