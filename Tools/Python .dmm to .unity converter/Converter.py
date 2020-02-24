import os

# Changes the file extension so that the program can read it (not really needed but good to look over as a human)
Fconv = True  # Change to False later
for file in os.listdir('.'):
    for x in range(len(file) - 1):
        if file[x - 1:x] == ".":
            if file[x:x + 3] == "dmm":
                os.rename(file, file[0:len(file) - 3] + "txt")
                mf = file[0:len(file) - 3] + "txt"
                Fconv = True
                break
# Dev bypass, this removes the need for the conversion process to allow rapid testing of code
mf = "cyberiad.txt"
# Creates the "base" of the map (The prefabs and managers needed to make a map work)

#if Fconv:
    #uname = mf[0:len(mf) - 4] + ".unity"
    #open(uname, "x")
    #w = open(uname, "a")
    #e = open("Base_Data.txt", "r")
    #w.write(e.read())
    #w.close()
#else:
    #print("Error: No convertable .dmm files!")
# Reads data from the new .txt file and interprets the tile data
klst = ["turf","structure","machinery"]
tlst = ["simulated",]
if Fconv:
    fd = open(mf, "r")
    fd = fd.read()
    for x in range(len(fd)):
        print(x)
        print(len(fd))
        if fd[x:x+1] == "\"":
            y = x
            for y in range(len(fd)):
                if fd[y+5:y+6] == "\"":
                    y = y + 5
# defunct until I somehow figure out a way to automatically set defines for tiles

