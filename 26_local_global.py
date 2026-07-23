# Global variable
x = 10

def fun():
    # Local variable
    y = 20
    print("Global =", x)
    print("Local =", y)

fun()

print("Global =", x)