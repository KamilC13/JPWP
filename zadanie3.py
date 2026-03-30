numbers = range(100_000)
cubes_list = []

for x in numbers:
    if x % 5 == 0:
        cubes_list.append(x**3)

total_sum = sum(cubes_list)
max_value = max(cubes_list)

print("Suma:", total_sum)
print("Największa wartość:", max_value)

#Zrefaktoryzuj powyższy kod, całkowicie usuwając pętlę 'for' oraz listę 'cubes_list', która niepotrzebnie zajmuje pamięć.
#Oblicz 'total_sum', wpisując wyrażenie generatorowe z odpowiednim warunkiem 'if' bezpośrednio do funkcji sum() (pamiętaj o braku nawiasów kwadratowych!).
#W analogiczny sposób oblicz 'max_value', wpisując wyrażenie generatorowe prosto do funkcji max().
#Uruchom kod i upewnij się, że wyniki wypisywane na konsoli pozostały takie same.
