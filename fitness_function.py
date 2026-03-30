def styblinski_tang(x_list):
    total = 0
    for x in x_list:
        total += (x**4 - 16*x**2 + 5*x)
    return 0.5 * total

def decode(binary_array, a, b, m):
    decimal_val = 0
    for bit in binary_array:
        decimal_val = (decimal_val << 1) | bit
    return a + decimal_val * (b-a) / (2**m - 1)

#def hypersphere(x_list):
    return sum(x**2 for x in x_list)