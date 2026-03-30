total = sum([x for x in range(1_000_000) if x % 3 == 0])
print("Suma:", total)

#Zrefaktoryzuj kod zgodnie z dobrymi praktykami przekazywania generatorów.
#Przekaż generator bezpośrednio do funkcji sum(), usuwając nawiasy kwadratowe.
#Sprawdź, czy wynik po refaktoryzacji pozostał ten sam.
