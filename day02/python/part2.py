"""
thinking:
it was easier to refactor and check every possible combination

"""


levels = []
safe_count = 0

with open("input.txt", "r") as file:
    for line in file:
        level = line.strip().split()
        levels.append(level)


# checks to see if it;s a valid difference, based on ascending or decending
def is_difference_valid(prev, curr, ascending):
    diff = int(curr) - int(prev)
    if ascending:
        return 1 <= diff <= 3
    else:
        return -3 <= diff <= -1


def check_level_safety(level):
    ascending = int(level[0]) < int(level[1])

    for i in range(len(level) - 1):
        if not is_difference_valid(level[i], level[i + 1], ascending):
            return False
        
    return True


def try_remove_element_and_check(level):
    # remove one element and see if it's valid
    for i in range(len(level)):
        new_level = level[:i] + level[i+1:]
        if check_level_safety(new_level):
            return True
    return False


for level in levels:
    if check_level_safety(level) or try_remove_element_and_check(level):
        safe_count += 1


print(safe_count)



