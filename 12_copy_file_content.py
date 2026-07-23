s = open("source.txt", "r")
d = open("copy.txt", "w")

d.write(s.read())

s.close()
d.close()

print("File copied successfully!")