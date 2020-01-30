# lights-out
Computing solutions to the Lights Out game using picosat.

## Description

The Lights Out puzzle game is very well described [here](https://www.jaapsch.net/puzzles/lights.htm).

The classic version of the game is like this: you have a grid of lights/buttons and you can toggle any of them, but the north, west, east and south neighbours are toggled at the same time. The goal is to turn off all the lights.

I was curious how many solutions existed for the case when you start with all the lights on.

It is trivial to notice that the state of the light only changes if there is an odd number of toggles affecting this light. So we can treat this as an exclusive-or (XOR) combination of light toggles.

So a state of any light in the middle of the board is: this-light-toggled XOR N-neighbor-toggled XOR E-neighbor-toggled XOR W-neighbor-toggled XOR S-neighbor-toggled. Lights on corners and edges have fewer neighbors. We want to generate a boolean formula that is true if a certain combination of lights are toggled. A toggled button has a boolean value of true, untoggled is false).

It is easy to write the formula using XOR, however picosat requires a formula in CNF (Conjunctive Normal Form). So I wrote a short Python program to generate all these XOR formulas for individual lights as conjunctions of alternatives.

After running picosat I was able to determine that the classic 5x5 game with "all lights on" starting state has exactly 4 solutions (actually 1 with rotational symmetry). I could check the numbers of solutions for larger grids as well.

In fact it is proven that the solution exists for every grid size and the proof can be found on the [maths page](https://www.jaapsch.net/puzzles/lomath.htm) of the site mentioned previously.

## Usage

```bash
python3 gridsat.py 6 > 6x6.cnf
picosat --all 6x6.cnf 
```

## Output

```
s SATISFIABLE
v 1 -2 3 4 -5 6 -7 8 9 10 11 -12 13 14 15 16 17 18 19 20 21 22 23 24 -25 26 27
v 28 29 -30 31 -32 33 34 -35 36 0
s SOLUTIONS 1

```

## Z3 as the alternative

Z3 has a SMT solver which can also be used to solve SAT. 
The advantage over picosat is that first of all there is
no intermediate step since Z3 solver has Python bindings. 
Moreover you can use typical boolean operators (Or, And, Xor, Not)
when specifying the constraints instead of CNF. 

## Usage Z3

```
python3 solvelights.py 9
```

## Another alternative - Sympy

Sympy can be used for symbolic computation and also
satisfability. Boolean operators can be used similar to Z3.
An advantage over Z3 is that satisfiable() function returns
a generator of models so getting all solutions is easier.
Unfortunately Sympy logic solver seems to be much slower than Z3.
At least you can use Sympy `to_cnf()` to transform a logic
formula to CNF and use it as input by a standalone solver.

## Usage Sympy

```
python3 sympylights.py 9
```

## Other useful links

My JavaScript implementation of the [Lights Out game](http://quiath.bitbucket.io/touch).
