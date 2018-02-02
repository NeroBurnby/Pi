from decimal import Decimal as Dec, getcontext as gc

def pi_generator(max_value):
    gc().prec = max_value                           #used to set precision and to enable decimal division
    M, L, X, K, S = 1, 13591409, 1, 6, 13591409
    if max_value <= 100:
        for k in range(1, max_value+1):
            M = M * (K**3 - 16*K)/(K+1)**3
            L = L + 545140134
            X = X*(-262537412640768000)
            S = S + (Dec(M*L)/X)
            K = K + 12
            pi = 426880 * Dec(10005).sqrt()/S
        return pi
    else:
        print("Enter a value less than 100")

reqd_value = int(input("Please enter the no of decimal places you require"))
Dec(pi_generator(reqd_value))
