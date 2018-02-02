BBox-Label-Tool
===============

A simple tool for labeling object bounding boxes in images, implemented with Python Tkinter.

**Updates:**
- 2017.5.21 Check out the ```multi-class``` branch for a multi-class version implemented by @jxgu1016

**Screenshot:**
![Label Tool](./screenshot.png)

Data Organization
-----------------
LabelTool  
|  
|--main.py   *# source code for the tool*  
|  
|--Images/   *# direcotry containing the images to be labeled*  
|  
|--Labels/   *# direcotry for the labeling results*  
|  
|--Examples/  *# direcotry for the example bboxes*  

Environment
----------
- python 2.7
- python PIL (Pillow)

Run
-------
$ python main.py

Usage
-----
0. The current tool requires that **the images to be labeled reside in /Images/001, /Images/002, etc. You will need to modify the code if you want to label images elsewhere**.
1. Input a folder number (e.g, 1, 2, 5...), and click `Load`. The images in the folder, along with a few example results will be loaded.
2. To create a new bounding box, left-click to select the first vertex. Moving the mouse to draw a rectangle, and left-click again to select the second vertex.
  - To cancel the bounding box while drawing, just press `<Esc>`.
  - To delete a existing bounding box, select it from the listbox, and click `Delete`.
  - To delete all existing bounding boxes in the image, simply click `ClearAll`.
3. After finishing one image, click `Next` to advance. Likewise, click `Prev` to reverse. Or, input an image id and click `Go` to navigate to the speficied image.
  - Be sure to click `Next` after finishing a image, or the result won't be saved. 


ProcessImages.workflow is an automator script to do the following in order:
    - 1. Get the images to work on
    - 2. Change the type of the images to JPEG format
    - 3. Change extension of all files to .JPEG (some files will have .jpg and .JPG etc.) because the BBox tool will accept only *.JPEG extension files.
    - 4. Scale all the images to 320 px in largest side so that Bbox tool will have a neat image to work on and it will be easy for ML training as well.
    

process.py file is from https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/. This file randomly categorizes an image into training or test data based on the percentage configured in the script for testing. The output of this is fed into darknet for training purpose


check.py - Jinesh authored this initially. check.py file is needed to see if every image file is properly associated with a text annotation file. The script finally copies only those image files for which it has a corresponding text annotation. Multiple annotation in a single image file and the corresponding image files are moved into a separate folder to keep it clean.


Added convert.py from https://github.com/Guanghan/darknet/blob/master/scripts/convert.py with modifications within it. The basic purpose of this script is to convert the BBox label annotation into Yolo format
