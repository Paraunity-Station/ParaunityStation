import os
# Changes the file extension so that the program can read it (not really needed but good to look over as a human)
Fconv = False
for file in os.listdir('.'):
    for x in range(len(file) - 1):
        if file[x-1:x] == ".":
            if file[x:x+3] == "dmm":
                os.rename(file, file[0:len(file)-3] + "txt")
                mf = file[0:len(file)-3] + "txt"
                Fconv = True
                break
# Creates the "base" of the map (The prefabs and managers needed to make a map work)

if Fconv:
    uname = mf[0:len(mf) - 4] + ".unity"
    open(uname, "x")
    w = open(uname, "a")
    e = open("Essential_Data.txt", "r")
    w.write(e.read())
    w.close()
else:
    print("Error: No convertable .dmm files!")
# Reads data from the new .txt file and interprets the tile data
if Fconv:
    dmd = open(mf, "r")
    print(dmd.read())