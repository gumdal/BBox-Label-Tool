import os
from shutil import copyfile

labelFolder = "/obj/"
newLabelFolder = "/newObj/"
arr = os.listdir('./obj/')
for file in arr:
    if file.endswith ('.txt'):
        filePath = os.path.join(os.getcwd() +labelFolder, file)
        newfilePath = os.path.join(os.getcwd() +newLabelFolder, file)
        f = open(filePath, "r")
        fout = open (newfilePath, "w")
        lines = f.readlines()
        for line in lines:
            fout.write(line.replace ('0','21',1))
            #f.write (line.replace ('0','21',1))
        #with open(filePath) as fin, open(os.path.join(os.getcwd() +newLabelFolder, file), "w") as fout:
            #for line in fin:
                #fout.write(line.replace ('0','21',1))
                #f.write (line.replace ('0','21',1))
    else:
        copyfile (os.path.join(os.getcwd() + labelFolder, file), os.path.join(os.getcwd() + newLabelFolder, file))
        