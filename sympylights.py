import sys
from sympy.logic.boolalg import ITE, And, Xor, Or
from sympy import Symbol
from sympy.logic.inference import satisfiable

"""
Prints all solutions of lights out puzzle
for the size given as the command line parameter
"""

def main():
    n = 4 if len(sys.argv) < 2 else int(sys.argv[1]) 

    a = { 
        (i, j): Symbol("{}_{}".format(i, j))
        for i in range(n)
        for j in range(n)
    }
    #print(list(a))

    expr = None 

    for i in range(n):
        for j in range(n):
            z = a[(i, j)]
            if i > 0: z = Xor(z, a[(i - 1, j)])
            if j > 0: z = Xor(z, a[(i, j - 1)])
            if i < n - 1: z = Xor(z, a[(i + 1, j)])
            if j < n - 1: z = Xor(z, a[(i, j + 1)])

            if expr is None:
                expr = z
            else:
                expr = And(expr, z)



    cnt = 0
    models = satisfiable(expr, all_models = True)

    for m in models:
        cnt += 1
        print("Solution {}".format(cnt))
        #print(sol.model())

        for i in range(n):
            s = "".join(
                ".X"[m[a[(i, j)]]]
                for j in range(n)
               ) 
            print(s)

    print("Solutions for {}: {}".format(n, cnt))

if __name__ == "__main__":
    main()
