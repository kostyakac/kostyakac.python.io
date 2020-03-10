import shutil
actionCheck = True
while(True):
    while(actionCheck == True):
        action = input("Vvedite operacio (file/dir): ")
        if(action == "file" or action == "File" or action == "FILE"):
            actionCheck = False
        elif(action == "dir" or action == "Dir" or action == "DIR"):
            actionCheck = False
        else:
            print("You don'twibrali operacio or ohibka")
            print("Povtorite operacio")
    onePath = input("Vvedite put kotorii nugno coping: ")
    twoPath = input("Vvedite put kotorii nugno pomestit: ")
    try:
        if(action == "file" or action == "File" or action == "FILE"):
            shutil.copy2(onePath, twoPath)
            actionCheck = True
        elif(action == "dir" or action == "Dir" or action == "DIR"):
            shutil.copytree(onePath, twoPath)
            actionCheck = True
        else:
            print("You don'twibrali operacio or ohibka")
            actionCheck = True
    except (NotADirectoryError):
        print("Alert - You vibral fail, a not directorii (NotADirectoryError)")
        actionCheck = True
    except (FileNotFoundError):
        print("Alert - Fail not found (FileNotFoundError)")
        actionCheck = True