n = int(input())
input_data =  []
output = []
#читаем ввод
for i in range(n):
    str_input = input()
    str_arr = str_input.split(" ")
    if(len(str_arr)) >1:
        input_data.append((str_arr[0], int(str_arr[1])))
    else:
        input_data.append((str_arr[0]))
"""
queue_in = []
queue_out = []

for operation in input_data:
    op_type = operation[0]
    if op_type == "+":#add to normal queue
        queue_in.append(operation[1])
    elif op_type == "*":#add to priority queue
        mod = (len(queue_in) + len(queue_out))%2
        pos = int(round((len(queue_in) + len(queue_out))/2,0)) - len(queue_out)
        if pos >= 0:
            for _ in range(pos):
                queue_out.append(queue_in.pop(0))
        else:
            for _ in range(-pos-mod):
                queue_in.insert(0, queue_out.pop())
        queue_out.append(operation[1])
    else: #remove from queue
        if(len(queue_out) > 0):
            output.append(queue_out.pop(0))
        else:
            output.append(queue_in.pop(0))
"""

lst = []

for operation in input_data:
    op_type = operation[0]
    if op_type == "+":#add to normal queue
        lst.append(operation[1])
    elif op_type == "*":#add to priority queue
        lst.insert(len(lst)//2 + len(lst)% 2, operation[1])
    else: #remove from queue
        output.append(lst.pop(0))

for el in output:
    print(el)

