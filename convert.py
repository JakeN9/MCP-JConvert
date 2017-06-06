import os
import os.path
import time

startepoch = int(round(time.time() * 1000))

from pathlib import Path

print("Starting MCP-JConvert  (Jake Nelson 2017)\n")

cdict = {}

cfiles = ['fields.csv', 'methods.csv', 'params.csv']

for cfile in cfiles:
    for line in open(cfile, 'r'):
        cdict[line.split(",")[0]] = line.split(",")[1]
        
in_floc = []

for dirpath, dirnames, filenames in os.walk(".\in"):
    for filename in [f for f in filenames]:
        in_floc.append(os.path.join(dirpath, filename))


for convertfile in in_floc:

    if(not convertfile.replace(".\\in\\","").count("\\") == 0):
        try:
            os.makedirs(".\\out\\"+convertfile.replace(".\\in\\","").rsplit('\\',1)[0])
        except FileExistsError:
            print("!!! Warning attempted to create folder ("+".\\out\\"+convertfile.replace(".\\in\\","").rsplit('\\',1)[0]+") - Already exists !!!")

    print("\nWriting to \\out\\"+convertfile.replace(".\\in\\",""))
    outf = open(".\\out\\"+convertfile.replace(".\\in\\",""), "w")

    for line in open(convertfile,"r"):
        
        line2 = line
        

        for repl in cdict:
            line2 = line2.replace(repl, cdict[repl])

        outf.write(line2)

    outf.close()
    print("Done!\n")


print("Done writing files in "+str(int(round(time.time() * 1000))-startepoch)+" milliseconds!")
