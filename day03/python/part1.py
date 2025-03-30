# 2 pointer approach in find_valid_num is more efficient than my approach

def open_and_save_file():
  array_of_lines = []
  with open("input.txt", "r") as file:
      for line in file:
        array_of_lines.append(str(line))
  return array_of_lines

def find_valid_substring_indexes(string, substring):
    return [i for i in range(len(string)) if string[i:i+len(substring)] == substring]


lines = open_and_save_file()
mul_idx = []

for line in lines:
  mul_idx.append(find_valid_substring_indexes(line, "mul("))


# a number is valid if it's less than 1-3 digits, and in between mul(xxx,yyy)
# first check if ) is in the string
# then check for ,
# split around the comma to get possible numbers
# check the numbers are vaid, then mutliply if so

def find_valid_num(string):

    if ")" not in string:
        return 0

    content = string[4:string.find(")")]
    
    if "," not in content:
        return 0

    parts = content.split(",")
    if len(parts) != 2:
        return 0

    num1, num2 = parts

    if num1.isdigit() and num2.isdigit() and 1 <= len(num1) <= 3 and 1 <= len(num2) <= 3:
        return int(num1) * int(num2)

    return 0
   
sum = 0

# pass in indexs that begin with mul(
for i in range(len(lines)):
  for idx in mul_idx[i]:
    sum += find_valid_num(lines[i][idx:idx+12])

print(sum)
