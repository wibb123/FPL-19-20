import numpy as np

def knapSack(W, wt, val, n, m):
    K = np.array([[0 for x in range(W + 1)] for x in range(n + 1)],dtype='f')
    for i in range(n + 1):
        for w in range(W + 1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    result = K[n][W]
    w = W
    print("Maximum value is " + str(result))
    for i in range(n+1):
        if result <= 0:
            break
        elif result == K[n-1-i][w]:
            continue
        else:
            print(m[n-1-i])
            result = result - val[n-1-i]
            w = w - wt[n-1-i]

def knapSackE(W, wt, val, n, m, D):
    K = np.array([[[0  for x in range(D + 1)]for x in range(W + 1)] for x in range(n + 1)],dtype='f')

    for i in range(n + 1):
        for w in range(W + 1):
            for d in range(D + 1):
                if i==0 or w==0 or d==0:
                    K[i][w][d] = 0
                elif wt[i-1] <= w:
                    K[i][w][d] = max(val[i-1] + K[i-1][w-wt[i-1]][d-1], K[i-1][w][d])
                else:
                    K[i][w][d] = K[i-1][w][d]
    result = K[n][W][D]
    w = W
    d = D
    included = []
    print("Maximum value is " + str(result))
    for i in range(n+1):
        if result <= 0 or d==0:
            break
        elif int(result) == int(K[n-1-i][w][d]):
            continue
        else:
            print(result)
            print(K[n-1-i][w][d])
            included.append(m[n-1-i])
            result = result - val[n-1-i]
            w = w - wt[n-1-i]
            d = d - 1
    return included

def knapSackEE(W, wt, val, n, m, D):
    K = np.array([[[0 for x in range(D + 1)]for x in range(W + 1)] for x in range(n + 1)],dtype='f')

    for i in range(n + 1):
        for w in range(W + 1):
            for d in range(D + 1):
                if i==0 or w==0 or d==0:
                    K[i][w][d] = 0
                elif wt[i-1] <= w:
                    K[i][w][d] = max(val[i-1] + K[i-1][w-wt[i-1]][d-1], K[i-1][w][d])
                else:
                    K[i][w][d] = K[i-1][w][d]
    return K[n,0:W,D]