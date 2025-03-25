levels = []
safe_count = 0

with open("input.txt", "r") as file:
    for line in file:
        level = []
        level.append(line.strip())
        levels += level
        
for level in levels:
    level = level.split()

    # check if the first 2 element are decending
    ascending = False
    if int(level[0]) < int(level[1]):
        ascending = True
    
    is_safe = True
    for i in range(0, len(level) - 1):

        if ascending:
            if (int(level[i]) - int(level[i + 1])) < -3 or (int(level[i]) - int(level[i + 1])) >= 0:
                is_safe = False

        if not ascending:
            if (int(level[i]) - int(level[i + 1])) > 3 or (int(level[i]) - int(level[i + 1])) <= 0:
                is_safe = False

    if is_safe:
        safe_count += 1

print(safe_count)



