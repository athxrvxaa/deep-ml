def orthogonal_projection(v, L):
    dot_product = sum(v[i] * L[i] for i in range(len(v)))
    magnitude_squared = sum(x * x for x in L)

    result = [(dot_product / magnitude_squared) * x for x in L]

    return [round(x, 3) for x in result]