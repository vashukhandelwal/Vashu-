if gcd(a, b):
   if b == 0:
       return a
    else:
        return gcd(b ,a % b)
num1 = 56
num2 = 98
result = gcd(num1,num2)
print("The GCD of {num1} and {num2}")
