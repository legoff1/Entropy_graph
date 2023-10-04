import random

# Create a domain and a distribution
n = 128 # size of domain D 
points = list(range(n)) # The domain D
scores = [0.01]*n 
scores[-1] = 0.9
scores = [value / sum(scores) for value in scores]


nbr_T = 10 # number of points we want
nbr_K = 3 # number of sample for each digit
scores_no_zeros = [value + 0.0001 for value in scores] # avoid division by zero

K = [] 
T = random.choices(points, scores, k = nbr_T)
for sigma in T:
    k = []

    print("point sigma: ", sigma)

    sup = points[n-1]
    inf = 0
    middle = int(inf + (sup-inf+1)/2)

    while middle > inf:
        if sigma >= middle:
            inf = middle
        else: 
            sup = middle - 1 
        middle = int(inf + (sup-inf+1)/2)   

        scores_1 = [0]*n
        scores_1[inf: sup+1] = scores_no_zeros[inf: sup+1]
        scores_1 = [value / sum(scores_1) for value in scores_1]

        k.append(random.choices(points, scores_1, k = nbr_K))
        print("draw numbers between ",inf, " and ", sup)
    K.append(k)

print(K)