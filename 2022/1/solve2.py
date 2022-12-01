lines = open('input', 'r').readlines()
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

print(sum(largest))
