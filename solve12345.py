'''Solves the 12345 game'''
from itertools import permutations, product

# Operations allowed in the game
OPS = [lambda a, b: a + b,
       lambda a, b: a - b,
       lambda a, b: a * b,
       lambda a, b: int(a / b) if b != 0 and a % b == 0 else None, # ignore cases where not divisible
       lambda a, b: int(a ** b) if b >= 0 and b < 20 and a != 0 else None # ignore cases where too large/small
       ]
OP_NAMES = ['+', '-', '*', '/', '^']


def solve12345():
    '''Returns solution strings corresponding to the 12345 game via brute force'''
    # Dictionary for solutions
    solutions = {}

    # Try all permutations of numbers 1-5
    for nums in permutations(range(1,6), 5):
        numtup = nums
        # Try all combinations of the five allowed operators
        for ops in product(zip(OPS, OP_NAMES), repeat=4):
            optup, opnames = zip(*ops)
            # Try all orders of eliminating expressions
            for order in product(range(4), range(3), range(2), range(1)):
                # Copy numbers and operators for elimination
                numstrs, opstrs = map(lambda n : str(n), numtup), list(opnames)
                nums, ops = list(numtup), list(optup)
                # Keep track of whether expression produces a disallowed result
                bad = False
                # Eliminate operators and numbers in specified order
                for o in order:
                    # Eliminate expression by applying operator, then deleting operator and operands
                    nums[o] = ops[o](nums[o], nums[o+1])
                    numstrs[o] = '(%s%s%s)' % (numstrs[o], opstrs[o], numstrs[o+1])
                    del ops[o], nums[o+1], opstrs[o], numstrs[o+1]
                    # If disallowed result is produced (None), then break out of both loops
                    if nums[o] is None:
                        bad = True
                        break
                # Break out of outer loop on finding disallowed result
                if bad:
                    break
                # Collect answer and corresponding expression string
                ans = nums[0]
                exprstr = numstrs[0]
                if ans not in solutions:
                    solutions[ans] = []
                solutions[ans].append(exprstr)

    # Return solutions found
    return solutions


# Run solver on 1234
if __name__ == '__main__':
    sols = solve12345()

    # Get number of solutions for puzzles up to 200
    # UNCOMMENT LINES BELOW

    for i in range(201):
        if i not in sols:
            sols[i] = []
        print(i, len(sols[i]))
    

    # Solve puzzle for arbitrary number
    # UNCOMMENT LINES BELOW

    print(sols[187])
    print(sols[197])
