
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
def find_valid_num(string):
  print(string)
   
   
for i in range(len(lines)):
  for idx in mul_idx[i]:
    find_valid_num(lines[i][idx:idx+12])
