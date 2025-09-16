import math

# Vector operations

def add_vectors(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def subtract_vectors(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def magnitude(v):
    return math.sqrt(sum(a**2 for a in v))

def unit_vector(v):
    mag = magnitude(v)
    return [a / mag for a in v]

# Example
v1 = [2, 3]
v2 = [4, 1]

print("v1 + v2 =", add_vectors(v1, v2))
print("v1 - v2 =", subtract_vectors(v1, v2))
print("Dot product =", dot_product(v1, v2))
print("|v1| =", magnitude(v1))
print("Unit vector of v1 =", unit_vector(v1))
