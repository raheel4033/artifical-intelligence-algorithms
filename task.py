

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [1, 2, 3, 4, 5]


def div(a, b):
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i] > b[j]:
                num = int(int(a[i])/int(b[j]))
                if num == 4:
                    aid = a[i]
                    bid = b[j]
                    print("x is:",aid)
                    print("y is:",bid)
                    break
                else:
                    print("Didn't find resultant 4")


div(x, y)

