f = open("source.txt", "r")
text = f.read()

for ch in set(text):
    print(ch, ":", text.count(ch))

f.close()