# Write a function that takes the number n and returns a list of all the perfect squares between 0 and n. A perfect square is a number s such that k2 = s for some integer k. For example, get perfect should return the list [0, 1, 4, 9, 16, 25, 36] def get_perfect_squares(n):


def get_perfect_squares(n):

    squares = []
    for i in range(n):
        squares.append(i*i)
    return squares
p=get_perfect_squares(5)
print(p)