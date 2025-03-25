"""
thinking:
rather than having is_safe, we could re-check the level with element 'i + 1' removed
the code should be refactored so that checking levels can be easily repeated
"""


levels = []
safe_count = 0

with open("input.txt", "r") as file:
    for line in file:
        level = []
        level.append(line.strip())
        levels += level


def check_level_safety(level):

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

    return is_safe
    

for level in levels:
    level = level.split()
    if check_level_safety(level):
        safe_count += 1

print(safe_count)



