n = int(input("Input N"))
points_str = input("Input points")
points_splitted = points_str.split(" ")
points = []

for i in range(n-1):
    points.append((i, int(points_splitted[i])))

def merge_sort(ar: list):
   if len(ar) == 1:
       return ar
   elif len(ar) == 2:
       return sort(ar)
   else:
       ar1 = ar[:len(ar) / 2]
       ar2 = ar[len(ar) / 2:]
       ar1_sorted = merge_sort(ar1)
       ar2_sorted = merge_sort(ar2)
       return merge(ar1_sorted,ar2_sorted)


def merge(ar1: list, ar2:list):
    i = 0
    j = 0
    result = []
    while i<len(ar1) and j<len(ar2):
        #merging




def sort(ar: list):
    if ar[0][1]< ar[1][1]:
        return ar[::-1]
    else:
        return ar