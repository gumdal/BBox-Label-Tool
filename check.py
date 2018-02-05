#Jinesh authored this initially. check.py file is needed to see if every image file is properly associated with a text annotation file. The script finally copies only those image files for which it has a corresponding text annotation. Multiple annotation in a single image file and the corresponding image files are moved into a separate folder to keep it clean.

import os
from shutil import copyfile
labelFolder = "/Labels/004/"
imagesFolder = "/Images/004/"
arr = os.listdir('./Images/004/')
outputFolder = "/Result/"
multipleResultsFolder = "/multiple-result/"
print (arr)
outputDirectory = os.path.join(os.getcwd(), outputFolder)
multipleResultsDirectory = os.path.join(os.getcwd(), multipleResultsFolder)
for file in arr:
    # compose JPEG file name     
    textFile = file.replace(".JPEG",".txt")    
    jpegFile = os.path.join(os.getcwd() +imagesFolder, file)
    filePath = os.path.join(os.getcwd() +labelFolder, textFile)
    print ('Hello World!')
    print ('JPEG file exists: ' + str(os.path.isfile(jpegFile)))
    print ('Text file exists: ' + str(os.path.isfile(filePath)))
    if (os.path.isfile(jpegFile) and os.path.isfile(filePath)):
        print ('Both files exists')
        try:
            f = open(filePath, "r")
            #num_lines = sum(1 for line in f)
            print ("File contents: ")
            print (f)
            length = len(f.readlines())
            f.close()
            print(length)
            if (length <= 1 ):
                print("Less in length")
                #delete image and text file
                #os.remove(jpegFile)
                #f.close()
                #os.remove(filePath)
                #continue
            elif(length > 2):
                print("Moving this File to multiple result directory")
                #os.rename(jpegFile, os.path.join(os.getcwd(), imagesFolder) + "/" + "multiple/" + file)
                #os.rename(filePath, os.path.join(os.getcwd(), labelFolder) + "/" + "multiple/" + textFile)
                copyfile (jpegFile, os.path.join(os.getcwd() + multipleResultsFolder + "/images/", file))
                copyfile (filePath, os.path.join(os.getcwd() + multipleResultsFolder + "/labels/", textFile))
            else:
                print("Moving this File to result directory")
                copyfile (jpegFile, os.path.join(os.getcwd() + outputFolder + "/images/", file))
                copyfile (filePath, os.path.join(os.getcwd() + outputFolder + "/labels/", textFile))
        except Exception as e:
            print(e)
            #delete file
            #os.remove(jpegFile)
    else:
        print ("Image and text counterpart not found!")
        print ("JPEG File: " + jpegFile)
        print ("Text File: " + filePath)
