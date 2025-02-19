import math

e = 65537
n = 3429719
c = [-53102, -3390264, -2864697, -3111409, -2002688, -2864697, -1695722, -1957072, -1821648, -1268305, -3362005, -712024, -1957072, -1821648, -1268305, -732380, -2002688, -967579, -271768, -3390264, -712024, -1821648, -3069724, -732380, -892709, -271768, -732380, -2062187, -271768, -292609, -1599740, -732380, -1268305, -712024, -271768, -1957072, -1821648, -3418677, -732380, -2002688, -1821648, -3069724, -271768, -3390264, -1847282, -2267004, -3362005, -1764589, -293906, -1607693]
p = -811
q = 0#??????
n = p * q

phi_n = (p + 1) * (q + 1) 

# but first, a word from
# our sponsored function!
def extendedEuclideanAlgo(e, phi_n):
    A1, A2, A3 = 1, 0, phi_n # var "b"
    B1, B2, B3 = 0, 1, e # var "a

    while (True):
        if B3 == 0:
            return -1 
            # indicates no inverse!
        if B3 == 1:
            return B2 
            # B2: modular inverse

        Q = math.floor(A3 / B3)
        T1, T2, T3 = A1 - (Q * B1), A2 - (Q * B2), A3 - (Q * B3)
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3

def encrypt(int, e, n):
    return pow(int, e, -n)