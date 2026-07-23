# add()
s = {1, 2, 3}
s.add(4)
print(s)

# update()
s.update([5, 6])
print(s)

# copy()
a = s.copy()
print(a)

# pop()
s.pop()
print(s)

# remove()
s.remove(2)
print(s)

# discard()
s.discard(10)   
print(s)

# clear()
b = {1, 2, 3}
b.clear()
print(b)

# union()
x = {1, 2, 3}
y = {3, 4, 5}
print(x.union(y))

# intersection()
print(x.intersection(y))

# difference()
print(x.difference(y))