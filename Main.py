def sumOfOddNumbers(a,b):
    b -= (1 + b % 2)
    if a % 2 == 0: a -= 2;
    a >>= 1
    b >>= 1;
    a += 1
    b += 1
    return (b * b - a * a) % 10000007;
