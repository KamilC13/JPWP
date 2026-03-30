logs = [
    "INFO: Start aplikacji",
    "WARNING: Mało pamięci",
    "ERROR: Brak połączenia z bazą",
    "INFO: Zakończenie pracy",
    "ERROR: Plik nie istnieje"
]

#Napisz od zera funkcję 'filter_errors(log_list)', która będzie generatorem.
#Pętlą 'for' przejdź przez przekazane logi i użyj 'yield', jeśli dany log zawiera słowo "ERROR".
#Przetestuj generator, przekazując do niego listę 'logs' w pętli 'for' i drukując wyniki.