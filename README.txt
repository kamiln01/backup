Skrypt automatyzujący tworzenie kopii zapasowej

Skrypt:
- umożliwia automatyczne tworzenie kopii zapasowej danych z wybranego folderu i zapisywanie ich na dysku zewnętrznym. 
- korzysta z wbudowanych bibliotek Pythona takich jak shutil i os, aby tworzyć archiwum i łączyć ścieżki do pliku z kopią zapasową.
- wymaga instalacji Pythona w wersji 3.x oraz bibliotek shutil i os.

Instrukacja obsługi:
Otworzyć skrypt w dowolnym edytorze tekstu, np. w Notatniku lub w PyCharm.
W linii 7 wybrać ustawić scieżkę folderu do zbackupowania.
W linii 10 wybrać ścieżkę do miejsca, w którym mają zostać zapisane kopie zapasowe.
Opcjonalnie, zmienić format nazwy pliku kopii zapasowej w linii 13, np. z 'backup_{}.zip' na 'backup_{}_mydata.zip'.
Uruchomić skrypt czekać, aż zostanie utworzona kopia zapasowa. Po zakończeniu działania skryptu zostanie wyświetlony komunikat z potwierdzeniem utworzenia kopii zapasowej.

Script Automating Backup Creation

Script:
- enables automatic backup of data from a selected folder and saving it on an external drive.
- utilizes built-in Python libraries such as shutil and os to create an archive and concatenate file paths for the backup.
- requires the installation of Python version 3.x and the shutil and os libraries.

Instruction Manual:
Open the script in any text editor, such as Notepad or PyCharm.
In line 7, set the path of the folder to be backed up.
In line 10, choose the path where the backups should be saved.
Optionally, change the backup file name format in line 13, e.g., from 'backup_{}.zip' to 'backup_{}_mydata.zip'.
Run the script and wait until the backup is created. Upon completion, a message confirming the backup creation will be displayed.

Created by kamiln01






