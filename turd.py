

fac_tab = {0:1, 1:1}
def factorial(n):
    f = 1
    for k in range(n, 0, -1):
        if k in fac_tab:
            break
    for i in range(k+1, n+1):
        fac_tab[i] = i * fac_tab[i-1]
    return fac_tab[n]

ir_tab = {0:0, 1:1, 2:1}
def irreducible(n):
    if n in ir_tab: return ir_tab[n]
    if n-1 not in ir_tab:
        for j in range(2, n-1): irreducible(j)  # avoid stack overflow
    ir_tab[n] = factorial(n) - sum( [factorial(i)*irreducible(n-i) for i in range(1, n)] )
    return ir_tab[n]
