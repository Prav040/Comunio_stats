import datetime
import os
import time

def run_ipynb(filename):
    # Funktion, um eine .ipynb-Datei auszuführen
    os.system(f'jupyter nbconvert --execute {filename}')

def wake_up_computer():
    # Funktion, um den Computer zu starten
    os.system("wakeonlan <MAC-Adresse des Computers>")

def shut_down_computer():
    # Funktion, um den Computer herunterzufahren
    os.system("shutdown /s /t 0")

def check_idle_time():
    # Funktion, um die Dauer der Inaktivität zu überprüfen
    idle_time = 0
    while True:
        # Schleife, die unendlich läuft
        idle_time += 1
        # Erhöhe die Inaktivitätsdauer um 1 Minute
        if idle_time == 15:
            # Wenn die Inaktivitätsdauer 15 Minuten erreicht hat, fahre den Computer herunter
            shut_down_computer()
            break
        # Warte eine Minute, bevor die Schleife erneut ausgeführt wird
        time.sleep(60)

while True:
    # Schleife, die unendlich läuft
    now = datetime.datetime.now()
    if now.hour == 12 and now.minute == 0:
        # Wenn es 12 Uhr mittags ist, führe die .ipynb-Datei aus
        run_ipynb('filename.ipynb')
    elif now.hour == 11 and now.minute == 50:
        # Wenn es 10 Minuten vor 12 Uhr mittags ist, starte den Computer
        wake_up_computer()
        check_idle_time()
    # Warte eine Minute, bevor die Schleife erneut ausgeführt wird
    time.sleep(60)