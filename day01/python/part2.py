left_array = []
right_dict = {}
total = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split("   ")
        left_array.append(int(line[0]))

        right_dict.setdefault(int(line[1]), 0)
        right_dict[int(line[1])] += 1

for number in left_array:
    if number in right_dict:
        total += right_dict[number] * number

print(total)
