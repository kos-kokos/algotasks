n = int(input("Input N"))
points_str = input("Input points")
points_splitted = points_str.split(" ")
points = []

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
    return t2[1] > t1[1]

def sort(ar: list):
    if ar[0][1]< ar[1][1]:
        return ar[::-1]
    else:
        return ar


for i in range(n):
    points.append((i, int(points_splitted[i])))
print(merge_sort(points))