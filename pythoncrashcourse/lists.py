bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())
print(bicycles[-1].title())

# bicycles[0] = "bsa"
# print(bicycles)

bicycles.append("bsa")

print(bicycles)

bicycles.insert(0, "bsa")

print(bicycles)

del bicycles[0]

print(bicycles)

pop_bicycle = bicycles.pop()

print(pop_bicycle)

pop_bicycle = bicycles.pop()

print(pop_bicycle)

bicycles.remove("redline")

print(bicycles)

bicycles.sort()

print(bicycles)
