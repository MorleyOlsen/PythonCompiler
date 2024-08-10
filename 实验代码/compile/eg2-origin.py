def solve_chicken_rabbit(total_heads, total_legs):
    # Chicken has 2 legs, rabbit has 4 legs
    for chickens in range(total_heads + 1):
        rabbits = total_heads - chickens
        if (chickens * 2 + rabbits * 4) == total_legs:
            return chickens, rabbits
    return None, None

total_heads = 35
total_legs = 94
chickens, rabbits = solve_chicken_rabbit(total_heads, total_legs)

if chickens is not None and rabbits is not None:
    print(f"Number of chickens: {chickens}, Number of rabbits: {rabbits}")
else:
    print("No solution found")
