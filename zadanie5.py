total = sum(x for x in range(1_000_000) if x % 3 == 0)

print("Suma (dobrze zoptymalizowana):", total)
def infinite_evens():
    pass

#Uzupełnij funkcję 'infinite_evens', aby generowała nieskończony ciąg liczb parzystych (0, 2, 4, 6...).
#Użyj w środku nieskończonej pętli 'while True' oraz słowa kluczowego 'yield'.
#Utwórz instancję generatora, przypisz do zmiennej i użyj 'next()' 4 razy, aby wydrukować wartości.