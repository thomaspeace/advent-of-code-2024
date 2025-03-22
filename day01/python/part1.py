left_array = []
right_array = []
total = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split("   ")
        left_array.append(int(line[0]))
        right_array.append(int(line[1]))

left_array.sort()
right_array.sort()

while len(left_array) > 0:
    total += abs(left_array.pop(0) - right_array.pop(0))

print(total)
