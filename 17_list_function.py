# List Functions Example

# i) list()
l = list((10, 20, 30))
print("list() =", l)

# ii) len()
print("len() =", len(l))

# iii) count()
l.append(20)
print("After append:", l)
print("count(20) =", l.count(20))

# iv) index()
print("index(30) =", l.index(30))

# v) append()
l.append(40)
print("append() =", l)

# vi) insert()
l.insert(1, 15)
print("insert() =", l)

# vii) extend()
l.extend([50, 60])
print("extend() =", l)

# viii) remove()
l.remove(20)
print("remove() =", l)

# ix) pop()
l.pop()
print("pop() =", l)

# x) reverse()
l.reverse()
print("reverse() =", l)

# xi) sort()
l.sort()
print("sort() =", l)

# xii) copy()
new_list = l.copy()
print("copy() =", new_list)

# xiii) clear()
new_list.clear()
print("clear() =", new_list)