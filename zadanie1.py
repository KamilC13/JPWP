#zadanie1.py
def powers_of_two(n):
    result = []
    for i in range(n):
        result.append(2 ** i)
    return result

print("Wynik z listy:", powers_of_two(5))

#Zrefaktoryzuj powyższy kod, aby funkcja 'powers_of_two' stała się generatorem!
#Pozbądź się tworzenia i zwracania listy 'result'.
#Użyj słowa kluczowego 'yield', aby zwracać kolejne potęgi dwójki bezpośrednio w pętli.
#Przypisz wywołanie funkcji do zmiennej i użyj funkcji next(), aby pobrać 3 pierwsze wartości.
---------------------------------
