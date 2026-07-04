import random

# ═══════════════════════════════════════
#  STEP 1 — Fitness Function
# ═══════════════════════════════════════
def fitness_function(x):
    return (-x**2) / 10 + 3 * x


# ═══════════════════════════════════════
#  STEP 2 — Generate Chromosome
# ═══════════════════════════════════════
def generate_chromosome():
    chromosome = []
    for i in range(5):
        chromosome.append(random.randint(0, 1))
    return chromosome


# ═══════════════════════════════════════
#  STEP 3 — Decode Chromosome
# ═══════════════════════════════════════
def decode_chromosome(chromosome):
    x = 0
    for bit in chromosome:
        x = x * 2 + bit
    return x


# ═══════════════════════════════════════
#  STEP 4 — Roulette Wheel Selection
# ═══════════════════════════════════════
def calculate_probabilities(fitness_values):
    total_fitness = 0
    for f in fitness_values:
        total_fitness += f

    probabilities = []
    for f in fitness_values:
        probabilities.append(f / total_fitness)

    return probabilities


def roulette_wheel_selection(population, probabilities):
    spin = random.random()
    cumulative = 0

    for i in range(len(population)):
        cumulative += probabilities[i]
        if spin <= cumulative:
            return population[i]

    return population[-1]


# ═══════════════════════════════════════
#  STEP 5 — Crossover
# ═══════════════════════════════════════
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)

    child1 = []
    for i in range(crossover_point):
        child1.append(parent1[i])
    for i in range(crossover_point, len(parent2)):
        child1.append(parent2[i])

    child2 = []
    for i in range(crossover_point):
        child2.append(parent2[i])
    for i in range(crossover_point, len(parent1)):
        child2.append(parent1[i])

    return child1, child2


# ═══════════════════════════════════════
#  STEP 6 — Mutation
# ═══════════════════════════════════════
def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)

    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0

    return chromosome


# _______________________________________
#  STEP 7 — Main GA Loop
# _______________________________________
def genetic_algorithm():

    # Generate initial population
    population_size = 10
    population = []
    for i in range(population_size):
        population.append(generate_chromosome())

    generation = 1

    while True:

        print(f"\n===== Generation {generation} =====")

        # ── Decode and calculate fitness for everyone
        fitness_values = []
        for chromosome in population:
            x       = decode_chromosome(chromosome)
            fitness = fitness_function(x)
            fitness_values.append(fitness)
            print(f"  {chromosome}  x={x:2}  fitness={fitness:.2f}")

        # ── Find best fitness this generation
        best_fitness = fitness_values[0]
        for f in fitness_values:
            if f > best_fitness:
                best_fitness = f

        print(f"  Best fitness this generation: {best_fitness:.2f}")

        # ── Check termination condition
        # Stop when best fitness >= 90% of maximum possible
        # Maximum f(x) occurs at x=15 → f(15) = 22.5
        max_possible = 22.5
        if best_fitness >= 0.9 * max_possible:
            print(f"\n✅ Termination condition met at generation {generation}!")
            break

        # ── Calculate selection probabilities
        probabilities = calculate_probabilities(fitness_values)

        # ── Select new population using roulette wheel
        selected = []
        for i in range(population_size):
            chosen = roulette_wheel_selection(population, probabilities)
            selected.append(chosen)

        # ── Create new population through crossover
        new_population = []
        for i in range(0, population_size, 2):
            parent1 = selected[i]
            parent2 = selected[i + 1]

            child1, child2 = crossover(parent1, parent2)

            new_population.append(child1)
            new_population.append(child2)

        # ── Apply mutation every 3 generations
        if generation % 3 == 0:
            print(f"  🔀 Mutation applied this generation!")
            for i in range(len(new_population)):
                new_population[i] = mutate(new_population[i])

        # ── Replace old population
        population   = new_population
        generation  += 1

    # ── Print final result
    fitness_values = []
    for chromosome in population:
        x       = decode_chromosome(chromosome)
        fitness = fitness_function(x)
        fitness_values.append(fitness)

    best_fitness    = fitness_values[0]
    best_index      = 0
    for i in range(len(fitness_values)):
        if fitness_values[i] > best_fitness:
            best_fitness = fitness_values[i]
            best_index   = i

    best_chromosome = population[best_index]
    best_x          = decode_chromosome(best_chromosome)

    print(f"\n🏆 Best Chromosome : {best_chromosome}")
    print(f"🏆 Best x value    : {best_x}")
    print(f"🏆 Best Fitness    : {best_fitness:.2f}")


genetic_algorithm()