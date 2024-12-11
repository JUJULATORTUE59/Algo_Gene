import random
import string

# Phrase cible
TARGET = "HELLO WORLD"
POPULATION_SIZE = 100
GENERATIONS = 1000
MUTATION_RATE = 0.01

# Générer un individu (chaîne aléatoire de la longueur de TARGET)
def generate_individual():
    individual = ''.join(random.choice(string.ascii_uppercase + ' ') 
        for _ in range(len(TARGET)))
    return individual

# Initialiser la population (liste d'individus)
def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(generate_individual())
    return population

# Calculer la fitness d'un individu (nombre de caractères corrects)
def fitness_function(individual):
    # Initialiser un compteur pour les caractères corrects
    score = 0
    
    # Comparer chaque caractère de l'individu avec celui de TARGET
    for i in range(len(TARGET)):
        if individual[i] == TARGET[i]:
            score += 1  # Si le caractère est correct, augmenter le score
    
    return score  # Retourner le nombre de caractères corrects


# Sélectionner deux parents
def selection(population):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)

    parent = max(tournament, key=fitness_function)

    return parent

# Croiser deux parents pour produire un enfant
def crossover(parent1, parent2,population):
    # Étape 1 : Choisir un point de coupure aléatoire
    point = random.randint(1, len(TARGET) - 1)  # Point entre 1 et len(TARGET) - 1
    
    parent1 = selection(population)
    parent2 = selection(population)

    while parent1 == parent2:
        parent2 = selection(population)

    # Étape 2 : Construire l'enfant
    child = parent1[:point] + parent2[point:]

    return child

# Appliquer une mutation à un individu
def mutate(individual):
    individual = list(individual) 
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            # Remplacer un caractère par un autre aléatoire
            individual[i] = random.choice(string.ascii_uppercase + ' ')
    return ''.join(individual)

# Algorithme génétique principal
def genetic_algorithm():
    population = initialize_population()
    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2,population)
            child = mutate(child)
            new_population.append(child)
        population = new_population
        # Afficher le meilleur individu de la génération
        best_individual = max(population, key=fitness_function)
        print(f"Génération {generation + 1}: {best_individual}, Fitness = {fitness_function(best_individual)}")
        if best_individual == TARGET:
            print("Phrase cible atteinte !")
            break

def test_generate_individual():
    individual = generate_individual()

    # Vérifier que la longueur de l'individu est correcte
    assert len(individual) == len(TARGET), f"Erreur : l'individu doit avoir {len(TARGET)} caractères."

    # Vérifier que tous les caractères de l'individu sont valides (lettres majuscules et espaces)
    for char in individual:
        assert char in string.ascii_uppercase + ' ', f"Erreur : caractère '{char}' invalide dans l'individu."

    print("Test passé : l'individu est de la bonne longueur et contient uniquement des caractères valides.")

# Tester la fonction initialize_population
def test_initialize_population():
    population = initialize_population()
    
    # Vérifier que la taille de la population est correcte
    assert len(population) == POPULATION_SIZE, f"Erreur : la population doit contenir {POPULATION_SIZE} individus."
    
    # Vérifier que chaque individu a la bonne longueur
    for individual in population:
        assert len(individual) == len(TARGET), "Erreur : un individu n'a pas la bonne longueur."
    
    print(f"Test passé : la population contient {POPULATION_SIZE} individus, tous de la bonne longueur.")

def test_fitness_function():
    # Test avec un individu parfait (doit avoir le même score que TARGET)
    individual_perfect = TARGET
    score_perfect = fitness_function(individual_perfect)
    assert score_perfect == len(TARGET), f"Erreur : le score de l'individu parfait doit être {len(TARGET)} mais il est de {score_perfect}."

    # Test avec un individu partiellement correct (par exemple, un individu proche de TARGET)
    individual_partial = "HE L O WORLD"  # Modifie ici pour qu'il ait quelques erreurs
    score_partial = fitness_function(individual_partial)
    print(f"Individu partiellement correct : {individual_partial}, Fitness = {score_partial}")

    # Vérification
    assert score_partial == 9, f"Erreur : le score pour l'individu partiel doit être 9, mais il est de {score_partial}."
    print("Test passé : la fonction de fitness fonctionne correctement.")

  # Tester la sélection
def test_selection():
    # Exemple de population
    population = [
        "HELLO WORLD",
        "HELLO W0RLD",
        "HE LLO WORLD",
        "HELLO XORLD",
        "HELLO YORLD",
    ]

    print("Population et leur fitness :")
    for individual in population:
        print(f"{individual}: Fitness = {fitness_function(individual)}")

    # Sélectionner un parent
    parent = selection(population)
    print(f"Parent sélectionné : {parent}, Fitness = {fitness_function(parent)}")  

# Lancer test 
#test_generate_individual()

# Lancer test de l'algorithme
#test_initialize_population()

# Lancer le test
#test_fitness_function()

# Lancer le test
#test_selection()

# Lancer l'algorithme génétique
genetic_algorithm()