def merge_sort(ar: list):
   if len(ar) == 1:
       return ar
   elif len(ar) == 2:
       return sort(ar)
   else:
       ar1 = ar[:int(len(ar)/2)]
       ar2 = ar[int(len(ar)/2):]
       ar1_sorted = merge_sort(ar1)
       ar2_sorted = merge_sort(ar2)
       return merge(ar1_sorted, ar2_sorted)


def merge(ar1: list, ar2:list):
    i = 0
    j = 0
    result = []
    while i<len(ar1) or j<len(ar2):
        if(i >= len(ar1)):
            result.append(ar2[j])
            j+=1
        elif j>= len(ar2):
            result.append(ar1[i])
            i+=1
        else:
            val1 = ar1[i]
            val2 = ar2[j]

            #merging
            if compareTuples(val1, val2):
                result.append(val1)
                i+=1
            else:
                result.append(val2)
                j+=1
    return result


def compareTuples(t1,t2):
    return t2[1] < t1[1]

def sort(ar: list):
    if ar[0][1]< ar[1][1]:
        return ar[::-1]
    else:
        return ar

n = int(input("Input N"))
points_str = input("Input points")
points_splitted = points_str.split(" ")
points = []

for i in range(n):
    points.append((i+1, int(points_splitted[i])))
sort_result = merge_sort(points)
result_str = ' '.join([str(x[0]) for x in sort_result])
print(result_str)