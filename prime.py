n=int(input("enter the value"))
if n > 1:
    for i in range (2, n//2):
        if (n % i) == 0:
            print(n, "is not prime")
            break
        else:
            print(n, "is  prime number")
    else:
            print(n, "is not prime")