f = open('postfix.in', 'r')
file_line = f.readline()
f.close()
stack = []
for val in  file_line.split(sep=" "):
    if val == "+" or val == "-" or val == "*":
        val2 = stack.pop()
        val1 = stack.pop()
        if(val == "+"):
            stack.append(val1 + val2)
        elif val=="-":
            stack.append(val1 - val2)
        else:
            stack.append(val1 * val2)
    else:
        stack.append(int(val))

result_file = open("postfix.out", 'w')
result_file.write(str(stack.pop()))
result_file.flush()
result_file.close()

