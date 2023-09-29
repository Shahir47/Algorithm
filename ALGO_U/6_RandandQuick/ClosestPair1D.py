import math
def CP_1D(ip, l, r, min_):
    if(l<r):
        m = l + (r-l)//2
        CP_1D(ip, l, m, min_)
        CP_1D(ip, m+1, r, min_)
        min_ = min(min_, ip[m+1]-ip[m])
        return min_ #Python uses lexical scoping; same variable shares same memory.


ip = [1,-5,9,13,2,-12,5,-3]
ip = sorted(ip)
print(ip)
print(CP_1D(ip, 0, len(ip)-1, math.inf))

