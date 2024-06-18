import math


def calculate_ratio(N, P, K):
    """
    Calculates the ratio between N, P, and K using gcd.
    Returns the values of N:P:K in a list.
    """
    gcd_value = math.gcd(math.gcd(N, P), K)
    ratio_N = N // gcd_value
    ratio_P = P // gcd_value
    ratio_K = K // gcd_value

    return [ratio_N, ratio_P, ratio_K]


# Example usage
N = 10
P = 5
K = 15

ratio_list = calculate_ratio(N, P, K)
print(f"Ratio N:P:K = {ratio_list}")
