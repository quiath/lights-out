from itertools import combinations
import sys

def xor(lst):
    n = len(lst)
    ans = [ lst ]
    m = 2
    while m <= n:
        for negated in combinations(lst, m):
            #print(negated)
            t = [ x * (-1 if x in negated else 1) for x in lst ]
            ans.append(t)
        m += 2

    return ans


def toi(x, y, n):
    return n * y + x + 1

def cnf_for_square(n):

    total = []

    for y in range(n):
        for x in range(n):
            indexes = []
            if y > 0: indexes.append(toi(x, y - 1, n))
            if x > 0: indexes.append(toi(x - 1, y, n))
            indexes.append(toi(x, y, n))
            if x < n - 1: indexes.append(toi(x + 1, y, n))
            if y < n - 1: indexes.append(toi(x, y + 1, n))

            #print(indexes)
            xorind = xor(indexes)
            total += xorind
    
    #print(total)

    print("c {n}x{n}".format(n=n))
    print("p cnf {var} {clauses}".format(var=n*n, clauses=len(total)))
    for t in total:
        t.append(0)
        print(" ".join([ str(x) for x in t ]))


def main():
    #for x in combinations(range(1, 3 + 1), 2):
    #    print(x)
    #print(xor([1, 2, 3]))

    n = 4 if len(sys.argv) < 2 else int(sys.argv[1])
    cnf_for_square(n)

if __name__ == "__main__":
    main()
