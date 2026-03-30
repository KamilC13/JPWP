#zadanie2.py
import sys

squares_list = [x**2 for x in range(10000)]
print("Rozmiar listy w pamięci (bajty):", sys.getsizeof(squares_list))

#Zrefaktoryzuj powyższy kod używając skróconej składni generatora!
#Zamień list comprehension na wyrażenie generatorowe (zmień odpowiednio nawiasy).
#Przypisz wynik do zmiennej 'squares_gen'.
#Wydrukuj za pomocą sys.getsizeof() rozmiar nowego obiektu i zobacz różnicę.
