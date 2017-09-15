
n = int(input())
str_in = input()
soldiers = []
result = [None]*10000
min = None
max = None
for s in str_in.split(" "):
    int_val = int(s)
    if min == None or int_val < min:
        min = int_val
    if max == None or int_val> max:
        max = int_val

    soldiers.append(int_val)
for soldier in soldiers:
    position = soldier - min
    if result[position] == None:
        result[position] = []
    result[position].append(str(soldier))
str_result = ""
for soldier_list in result:
    if not (soldier_list == None):
        if len(str_result) > 0:
            str_result+=" "
        str_result+=" ".join(soldier_list)
print(str_result)