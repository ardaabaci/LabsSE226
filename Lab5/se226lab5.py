def factorial(x):
    if x==0 or x==1:
        return 1
    return x*factorial(x-1)

term=lambda x, n: (x**n) / factorial(n)

def exp_x(x, n):
    total=0
    i=0
    while i<n:
        total+=term(x, i)
        i += 1
    return total

result=0
def alternating_sum(n):
    """
    Calculates Sn = 1 - 1/2 + 1/3 - ... recursively using a global variable.
    Logic: The function calls itself with n-1 until n=0.
    Sign Handling: Adds 1/n if n is odd, subtracts 1/n if n is even.
    """
    global result
    if n == 0:
        return
    if n%2 == 1:
        result += 1/n
    else:
        result -= 1/n
    alternating_sum(n - 1)
x_val=float(input())
n_val=int(input())
print(exp_x(x_val, n_val))
n2_val=int(input())
result = 0
alternating_sum(n2_val)
print(result)


