#Task 1
pos=int(input("Enter positive integers greater than 1: "))
step=0
c=pos
while c>1:
    print(c, end=" -> ")
    if c%2==0:
        c=c//2
    else:
        c=3*c+1
    step+=1
print(1)
print("Total steps:", step)

#Task 2
while True:
    n=int(input("\nEnter possitive integers between 10 and 100"))
                
    if 10<=n2<=100:
        break
    print("Invalid output. Enter between 10 and 100")   

f_count=0
b_count=0
total_count=0
for i in range(1, n + 1):
    if i%7==0:
        continue
    if i%3==0 and i%5==0:
        print("FizzBuzz")
        total_count +=1
    elif i%3==0:
        print("Fizz")
        f_count += 1
    elif i%5==0:
        print("Buzz")
        b_count += 1
    else:
        print(i)
print("Summary")
print("Fizz count:", f_count)
print("Buzz count:", b_count)
print("FizzBuzz count:", total_count)

#Task 3
n = int(input("\nPlease enter a number between 3 and 9: "))
for i in range(1, 2 * n):
    k=n-abs(n-i) # 
    print("*"*k)


