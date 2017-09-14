def is_open(s):
    return s == "(" or s == "{" or s == "["

def is_same_type(open, close):
    if open=="(" and close == ")":
        return True
    elif open=="{" and close =="}":
        return True
    elif open=="[" and close == "]":
        return True
    else:
        return False


def chesk(str):
    stack = []
    for s in str:
        if(is_open(s)):
            stack.append(s)
        else:
            if(len(stack)) == 0:
                return False
            else:
                from_stack = stack.pop()
                if not is_same_type(from_stack,s):
                    return False
    return len(stack) == 0

str = input()
result = chesk(str)
if(result):
    print("YES")
else:
    print("NO")