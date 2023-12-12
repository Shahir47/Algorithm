def R(D, i, j):
    if j<i:
        return 0
    sum_ = 0
    for k in range(i, j+1):
        sum_ += D[k]
    return sum_

def SodaHighway(E, D, left, right, distance):
    n = len(D)-1
    if(left<0 and right>n):
        return 0
    
    sum_L = sum_R = 0

    left = left - 1
    if left >= 0:
        distance += E[before_l] - E[left]
        student = R(D, 0, left) + R(D, before_l+1, n)
        sum_L = distance*student + SodaHighway(E, D, left, before_l+1, distance)

    right = right + 1
    if right <= n:
        distance += 

E = [20, 40, 60, 80, 100]
D = [10, 15, 30, 20, 5]
s = 2
print(SodaHighway(E, D, s, s, 0))