def collatz(num):
    for i in range(100):
        if num==1:
            print("The number of steps taken are:", i)
            break
        elif num%2==0:
            num=num//2
            print(num)
        else:
            num=(num*3 +1)
            print(num)

n=int(input("Enter the number"))
collatz(n)