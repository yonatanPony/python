def rec(n):
    if n == 1:
        return n
    else:
        return n*rec(n-1)

num = int(input("Enter your num: "))

if num <0 :
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print("The factorial of",num,"is",rec(num))