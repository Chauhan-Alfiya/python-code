
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

#alphabet

for i in range(5):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()

#star_patten
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()