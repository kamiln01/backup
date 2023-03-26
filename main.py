import shutil
import os
import datetime


# wybór folderu, który ma zostać zbackupowany
folder_to_backup = "ścieżka"

# wybór miejsca, na którym mają zostać zapisane kopie zapasowe
backup_drive = "ścieżka"

# tworzenie nazwy pliku z kopią zapasową na podstawie daty i czasu
backup_filename = "backup_{}.zip".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

# łączenie ścieżek do pliku z kopią zapasową
backup_path = os.path.join(backup_drive, backup_filename)

# tworzenie archiwum zip z wybranego folderu
shutil.make_archive(backup_path, 'zip', folder_to_backup)

# komunikat z potwierdzeniem utworzenia kopii zapasowej
print("Kopia zapasowa została utworzona i zapisana w {}.".format(backup_path))
