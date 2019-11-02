
if __name__ == '__main__':
    array = [1,2,3,3,4,4,5,5,6,6]
    res = []
    hashDict = {}
    for num in array:
        hashDict[num] = hashDict[num] + 1 if hashDict.get(num) else 1
    print(hashDict)
    for k, v in hashDict.items():
        if v == 1:
            res.append(k)
    print(res)