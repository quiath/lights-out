import sys
from z3 import *

"""
Prints all solutions of lights out puzzle
for the size given as the command line parameter
"""

def main():
    n = 4 if len(sys.argv) < 2 else int(sys.argv[1]) 

    a = { 
        (i, j): Bool("a_{}_{}".format(i, j))
        for i in range(n)
        for j in range(n)
    }
    #print(list(a))

    sol = Solver()

    for i in range(n):
        for j in range(n):
            z = a[(i, j)]
            if i > 0: z = Xor(z, a[(i - 1, j)])
            if j > 0: z = Xor(z, a[(i, j - 1)])
            if i < n - 1: z = Xor(z, a[(i + 1, j)])
            if j < n - 1: z = Xor(z, a[(i, j + 1)])

            sol.add(z)


            #z = Xor(a[(0, 0)], a[(0, 1)])
            #z = Xor(z, a[(0, 2)])

    cnt = 0

    while sol.check() == sat:
        print(sol.check())
        cnt += 1
        #print(sol.model())
        
        z = False

        for i in range(n):
            s = ""
            for j in range(n):
                v = a[(i, j)]
                s += ".X"[is_true(sol.model()[v])]
                
                if is_true(sol.model()[v]):
                    z = Or(z, Not(v))
                else:
                    z = Or(z, v)


            print(s)
        sol.add(z)
    print("Solutions for {}: {}".format(n, cnt))

if __name__ == "__main__":
    main()
