
grapes = list(map(int, input().split()))

n = int(input())

while len(grapes) > n:
    for count in range(n):
        for i in range(len(grapes)):
            grapes[i] += 1

        for i in range(len(grapes)):
            first = i == 0
            last = i == len(grapes) - 1

            if not first and not last:
                previousIndex = i - 1
                nextIndex = i + 1
                if grapes[i] > grapes[previousIndex] and grapes[i] > grapes[nextIndex]:
                    grapes[i] -=1
                    if grapes[previousIndex] > 0:
                        grapes[i] += 1
                        grapes[previousIndex] = max(grapes[previousIndex] - 2, 0)
                    if grapes[nextIndex] > 0:
                        grapes[i] += 1
                        grapes[nextIndex] = max(grapes[nextIndex] - 2, 0)

    grapes = list(filter(lambda a: a > n, grapes))
    
print(*grapes, sep=' ')