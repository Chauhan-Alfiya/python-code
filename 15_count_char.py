f = open("source.txt", "r")

text = f.read()

characters = len(text)
words = len(text.split())
lines = len(text.split("\n"))

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)

f.close()