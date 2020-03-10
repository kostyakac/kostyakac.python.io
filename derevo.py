import os
print("Derevo katalogov user: ")
print(os.environ)
print("Name Polzovatela: " + str(os.getlogin()))
print("Working derectoria: " + str(os.getcwd()))
systemOS = os.name
while(True):
    try:
        if(systemOS == "nt"):
            print("Our operation system: Windows")
        elif(systemOS == "posix"):
            print("Our operation system: Linux")
        elif(systemOS == "mac"):
            print("Our operation system: Mac")
        else:
            pass
        direct = input("Vvedite put k derectorii: ")
        print("Vaha derectoria" + direct)
        print(os.listdir(direct))
    except (FileNotFoundError):
        print("Alert - file not found (FileNotFoundError)")
    except (OSError):
        print("Alert -Sintaksis error(OSError)")