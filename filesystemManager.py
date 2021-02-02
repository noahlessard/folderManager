import os 
from pathlib import Path
import time

while True:
    
    
    path = Path("C:/Users/Administrator/Desktop/Zack\'s New World/backups").rglob('*.zip')



    fileArray = []
    nameArray = []

    for name in path:
        fileArray.append(os.path.getmtime(name))
        nameArray.append(name)
        print ('name= ', name, '\n')

    if len(nameArray) > 3:

        KeepNameNum = fileArray.index(max(fileArray))

        print(nameArray[KeepNameNum])

        for name in nameArray:
            if name != nameArray[KeepNameNum]:
                print("deleting ", name, "... \n")
                os.remove(name)
                continue
    else:
        time.sleep(10)
        continue
