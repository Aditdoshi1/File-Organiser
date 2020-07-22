import shutil
import os
import glob

def copy(newpath,file):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.copy(file, newpath)
    os.remove(file)

def folder(extension,fname):
    lists=glob.glob(extension)
    print(lists)
    for name in lists:
        if name=="organizer.py":
            print(name)
            continue
        copy(fname,name)

folder("*.py","Python Scripts")
folder("*.pptx","Documents/PowerPoint Presentations")
folder("*.java","Java Codes")
folder("*.c","C Codes")
folder("*.html","HTML")
folder("*.txt","Documents/Text Files")
folder("*.docx","Documents/Word Files")
folder("*.cpp","C++ Files")
folder("*.mp3","Music")
folder("*.mp4","Videos")
folder("*.xlsx","Documents/Excel Sheets")
folder("*.pdf","Documents/PDF Files")
folder("*.rar","Compressed files")
folder("*.zip","Compressed files")
images=["*.jp*","*.png","*.psd","*.bmp"]
for img in images:
    folder(img,"Images")