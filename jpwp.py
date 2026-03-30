# ==========================================
# PRZYKŁAD: LISTA VS GENERATOR
# ==========================================

print("=== LISTA ===")
numbers_list = [x for x in range(5)]
print(numbers_list)

print("\n=== GENERATOR ===")
numbers_gen = (x for x in range(5))
print(numbers_gen)  # nie pokazuje wartości!


# ==========================================
# ITERACJA (next)
# ==========================================

print("\n=== ITERACJA next() ===")
gen = (x for x in range(3))

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # StopIteration


# ==========================================
# GENERATOR Z yield
# ==========================================

print("\n=== GENERATOR (yield) ===")

def my_generator():
    print("Start")
    yield 1
    print("Środek")
    yield 2
    print("Koniec")

g = my_generator()

print(next(g))
print(next(g))
# print(next(g))  # StopIteration


# ==========================================
# LAZY EVALUATION (opóźnione obliczenia)
# ==========================================

print("\n=== LAZY EVALUATION ===")

import time

def heavy_computation():
    for i in range(3):
        print(f"Liczenie {i}...")
        time.sleep(1)
        yield i * 10

lazy = heavy_computation()

print("Generator utworzony (nic się nie liczy)")
print(next(lazy))  # dopiero teraz się liczy
print(next(lazy))


# ==========================================
# FILTROWANIE (if w generatorze)
# ==========================================

print("\n=== FILTROWANIE ===")

even_squares = (x**2 for x in range(10) if x % 2 == 0)

for val in even_squares:
    print(val)


# ==========================================
# ITERATOR (iter + next)
# ==========================================

print("\n=== ITERATOR ===")

data = [10, 20, 30]
it = iter(data)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # StopIteration


# ==========================================
# NIESKOŃCZONY GENERATOR
# ==========================================

print("\n=== NIESKOŃCZONY GENERATOR ===")

def infinite_counter(start=0):
    while True:
        yield start
        start += 1

counter = infinite_counter()

print(next(counter))
print(next(counter))
print(next(counter))


# ==========================================
# GENERATOR + FUNKCJE (sum)
# ==========================================

print("\n=== GENERATOR W FUNKCJI ===")

total = sum(x**2 for x in range(5))
print("Suma kwadratów:", total)


# ==========================================
# PODSUMOWANIE
# ==========================================

print("\n=== PODSUMOWANIE ===")
print("Lista -> wszystko w pamięci")
print("Generator -> elementy tworzone na bieżąco")
print("Lazy evaluation -> liczy tylko gdy trzeba")