# Should return the sum of integers 1, ..., n
def get_sum(n):
    sum = 0
    i = 1
    while i <= n:
        i += 1
        sum += i
        if i == n:
            return sum
        
assert get_sum(3) == 6
assert get_sum(10) == 55