def div(a, b):
    if a % b == 0:
        print(a ," is compeletely divisible by " , b)
    else:
        print(a ," is not divisible by " , b)

n1 = int(input("Enter value:"))
n2 = int(input("Enter value you want first value to divide it with:"))
div(n1, n2)
