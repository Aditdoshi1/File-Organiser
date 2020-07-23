import shutil
import os
import glob

def move(newpath,file):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.move(file, newpath)

def folder(extension,fname):
    lists=glob.glob(extension)
    print(lists)
    for name in lists:
        if name=="organizer.py":
            print(name)
            continue
        move(fname,name)
        
folder("*.exe", "Application Files & Executables")
folder("*.pptx", "Documents/PowerPoint Presentations")
folder("*.xlsx", "Documents/Excel Sheets")
folder("*.pdf", "Documents/PDF Files")
folder("*.txt", "Documents/Text Files")
folder("*.docx", "Documents/Word Files")
folder("*.py", "Python Scripts")
folder("*.java", "Java Codes")
folder("*.c", "C Codes")
folder("*.html", "HTML")
folder("*.cpp", "C++ Files")
folder("*.rar", "Compressed files")
folder("*.zip", "Compressed files")
folder("*.srt", "Subtitles")

videos = ["*.mp4", "*.avi", "*.gif", "*.amv", "*.m4v", "*.mpg", "*.mpeg"]
for video in videos:
    folder(video, "Videos")

audio = ["*.aac", "*.flac", "*.m4a", "*.mp3"]
for music in audio:
    folder(music, "Music")

images=["*.jp*", "*.png","*.psd","*.bmp"]
for img in images:
    folder(img, "Images")
