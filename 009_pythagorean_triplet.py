def get_triplets_up_to(max_a):
    for a in range(1, max_a):
        for b in range(1, a):
            c_squared = pow(a, 2) + pow(b, 2)
            c = c_squared ** (1/2)
            if c == int(c):
                yield {
                    "a": a, 
                    "b": b, 
                    "c": c, 
                    "sum": a + b + c,
                    "product": a*b*c
                } 

def find_triplets_with_sum(prod):
    triplets = get_triplets_up_to(prod)
    return [t for t in triplets if t["sum"] == prod]

print(find_triplets_with_sum(12))
print(find_triplets_with_sum(1000))
