def armstrong(n):
    s = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        s = s + digit ** 3
        temp = temp // 10

    if s == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

num = int(input("Enter number: "))
armstrong(num)