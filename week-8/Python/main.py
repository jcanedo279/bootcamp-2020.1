import numpy as np


def stoneCounter(inp):
    # Parse n and q list lengths
    nLen, inp = int(inp[: inp.index(" ")]), inp[inp.index(" ") + 1 :]
    qLen, inp = int(inp[: inp.index(" ")]), inp[inp.index(" ") + 1 :]
    # Parse n and q lists
    nqList = [int(nqItem) for nqItem in inp.split(" ")]
    n = nqList[:nLen]
    q = nqList[nLen:]

    # We create a list of how many stones we have at each day
    stonesPerDay = [n[0]]
    for numStones in n[1:]:
        stonesPerDay.append(numStones + stonesPerDay[-1])

    # Find on which day the query is from using np's searchsorted
    queryAnswer = [npHandle(n, stonesPerDay, qItem) for qItem in q]
    print(queryAnswer)


def npHandle(n, stonesPerDay, qItem):
    # Handle any edge cases (ie: qItem not in range of stonesPerDay)
    try:
        return n[np.searchsorted(stonesPerDay, qItem)]
    except:
        return f"{qItem} NA"


def strToList(s):
    return [int(sItem) for sItem in s.split(" ")]


def listToStr(l):
    return " ".join([str(lItem) for lItem in l])


# n = [1, 2, 3, 4, 5]
# q = [3, 8, 10, 14]

# input = f"{len(n)} {len(q)} {listToStr(n)} {listToStr(q)}"

# stoneCounter(input)


# n = [1, 0, 0, 0, 0]
# q = [0, 1, 2, 3, 4]

# input = f"{len(n)} {len(q)} {listToStr(n)} {listToStr(q)}"

# stoneCounter(input)


def smallestKRep(input):
    _, input = int(input[: input.index(" ")]), input[input.index(" ") + 1 :]
    nkList = [int(nkItem) for nkItem in input.split(" ")]
    n, k = nkList[:-1], nkList[-1]

    countMap = {}
    for nItem in n:
        if nItem in countMap:
            countMap[nItem] += 1
        else:
            countMap[nItem] = 1

    smallest = float("inf")
    for key, val in countMap.items():
        if val == k:
            if key < smallest:
                smallest = key
    return smallest


n = [1, 1, 1, 1, 2, 3, 3, 3, 3, 0, 0, 0, 0, 5]
k = 4

input = f"{len(n)} {listToStr(n)} {k}"

print(smallestKRep(input))
