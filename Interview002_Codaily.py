# given a string representing a sequence of N arrows, each pointing in one of the four cardinal directions: up("^"), down("v"), left("<"), or right (">"). write a function solution that, given a string S denoting the directions of the arrows, returns the minimum number of arrows that must be rated to make them all point in the same direction. for example: 1. Given S = "^vv<v", the function should return 2. After rotating both the first and fourth arrows downwards, all the arrows would point down.  Using Python to write this function.
# def solutions(S):
#     up_arrows = S.count("^")
#     down_arrows = S.count("v")
#     left_arrows = S.count("<")
#     right_arrows = S.count(">")
#
#     maximum_arrows = max(up_arrows, down_arrows, left_arrows, right_arrows)
#     min_rotation = len(S) - maximum_arrows
#     return min_rotation
#
#
# if __name__ == '__main__':
#     S = "^<>>^vvv><"
#     print(solutions(S))

#======#
# I am a programmer in a scientific team doing research into particles. As an experiment, you have measured the position of a single particle in N equally distributed moments of time. The measurement made in moment K is recorded in array A as A[K]. Now your job is to count all the periods of time when the movement of the particle was stable. Those are the periods during which the particle doesn't change its velocity: i.e. the difference between any two consecutive position measurements remains the same. Note that you need at least three measurements to be sure that the particle didn't change its velocity. for example, 1, 3, 5, 7, 9 is stable with velocity of 2. 0, 1 is not stable(you need at least 3 measurements), 1, 1, 2, 5, 7, is not stable, (velocity changes between measurements). more formally, your task is to find all the periods of time A[P], A[P+1], ..., A[Q] (of length at least 3) during which the movement of the particle is stable. Note that some periods of time might be contained in others. write a function: that given array A consisting of N integers representing the results of the measurements returns the number of periods of time when the movement of the particle was stable, the function should return -1 if the result exceeds 1000,000, 000. Using Python.
# for example A = [2, 2, ...,2] of length 10,000, the function should return 49985001. Example 2, if the array A = [-1, 1, 3, 3, 3, 2,3,2, 1, 0], it should return 5. Please check again the code and rewrite.

def solutions(A):

    numStable = 0
    n = len(A)
    if n < 3:
        return 0

    for x in range(n-1):
        base_value = A[x+1] - A[x]
        for y in range(x+2, n):
            if A[y] - A[y-1] == base_value:
                numStable += 1
            else: break

    return numStable if numStable < 1000000000 else -1

if __name__ == "__main__":
    # A = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
    A = [2] * 10000
    # A = [1, 3, 5, 7, 9]
    print(solutions(A))