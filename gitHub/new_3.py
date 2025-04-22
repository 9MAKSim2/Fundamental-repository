pq = [[0, 5], [1, 2], [3, 4],[2, 3], [3, 0], [6,9], [9,11], [9, 15]]
def sort(pq):
    pq.sort(key=lambda x: x[0])
    return pq

def gr(array, a, b):
    array = sort(array)
    totaly = []
    
    for x in array:
        is_there = []
        for y in array:
            if set(x).intersection(y) != set():
                is_there.append(list(set(x+y)))
        inter = []
        for y in is_there:
            inter += y
        totaly.append(set(inter))
   
    for x in range(len(totaly)):
        for y in range(len(totaly)):
            if x == y:
                continue
            if set(totaly[x]).issubset(totaly[y]):
                totaly[x] = []
            elif set(totaly[x]).intersection(totaly[y]):
                totaly[x] = set(list(totaly[x]) + list(totaly[y]))

    res = list(filter(None, totaly))
    for x in res:
        if a in x and b in x:
            print('Yes')
            break
        elif ((a in x) and (b not in x)) or ((a not in x) and (b in x)):
            print('No')
            break
    print(res)
print(gr(pq, 1, 6))