f = open("source.txt", "r")

for line in f:
    print(line[::-1])

f.close()