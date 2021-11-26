def Puzzle_Solve(k, S, U):
    for e in U.copy():
        if k == 1:
            if S == "bc":
                print("Solution found!")
        else:
            S += e
            U.discard(e)
            print(S, U, k)
            Puzzle_Solve(k-1, S, U)
        S = S.rstrip(S[-1])
        U.add(e)


Puzzle_Solve(3, "", {'a', 'b', 'c'})
