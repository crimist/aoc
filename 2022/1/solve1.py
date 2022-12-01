lines = open('input', 'r').readlines()
largest = 0
current = 0

for line in lines:
    data = line.strip()
    if data == "":
        if current > largest:
            largest = current
        
        current = 0
    else:
        current += int(data)

print(largest)
