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

## Looping

magicians = ["david", "alice", "carolina"]

for magician in magicians:
    print(magician)

## range

for value in range(1,5):
    print(value)

for value in range(2,11,2):
    print(value)

squares = []

for value in range(1,10):
    squares.append(value*value)

print(squares)

nums = range(1,100,3)

nums.sort(reverse=True)

print(nums)

print(max(nums))

squares = [value**2 for value in range(1,10)]

print(squares)