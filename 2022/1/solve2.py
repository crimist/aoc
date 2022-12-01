L = ["Geeks\n", "for\n", "Geeks\n"]

# Using readlines()
file1 = open('input', 'r')
lines = file1.readlines()

largest = [0,0,0]
current = 0

for line in lines:
    data = line.strip()
    if data == "":
        minLargest = min(largest)
        if current > minLargest:
            largest[largest.index(minLargest)] = current
        current = 0
    else:
        current += int(data)

print(largest)
print(sum(largest))
