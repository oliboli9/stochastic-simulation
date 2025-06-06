import matplotlib.pyplot as plt

def lcg(a, c, M, n, x0):
    """
    Linear Congruential Generator (LCG) for generating pseudo-random numbers.
    
    Parameters:
    a (int): multiplier
    c (int): shift
    M (int): modulus
    n (int): number of random numbers to generate
    x0 (int): initial seed (starting value)
    
    Returns:
    list: A list of n pseudo-random numbers
    """
    x = x0  # Initial seed
    random_numbers = []
    
    for _ in range(n):
        x = (a * x + c) % M
        random_numbers.append(x)
    
    return random_numbers
    
print(lcg(5,1,16,10,3))

numbers = lcg(5, 1, 16, 10000, 3)
bins = [i for i in range(10)]  # Bins from 0 to 16
plt.hist(numbers, bins=bins, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


