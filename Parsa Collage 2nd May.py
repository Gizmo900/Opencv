
#The program counts all files in an image folder, opens each image, prints its size, 
# adds up all widths and heights, and calculates the average width and height of the images.

from PIL import Image          # Imports Image from PIL so we can open and check image sizes
import cv2                     # Imports OpenCV library; 
import os                      # Imports os so we can work with folders and files

# This is the folder where the images are stored
path = "C:\\Users\\parsa\\Desktop\\Jetlearn coding\\Opencv\\Opencv images"

# Changes the current working folder to the image folder
os.chdir(path)

#Counts how many files are inside the current folder
imagecount = len(os.listdir('.'))

#Prints the number of files found in the current folder
print("Number of images/files:", imagecount)


meanwidth = 0     # Creates a variable to store the average width
meanheight = 0    # Creates a variable to store the average height

totalwidth = 0     # Creates a variable to store the total width of all images
totalheight = 0    # Creates a variable to store the total height of all images

# Loops throught each file in the folder
for i in os.listdir('.'):

    image = Image.open(os.path.join(path, i))  # Opens the image file using its full path
    imagewidth, imageheight = image.size       # Gets the width and height of the image 
    print("Image size:", image.size)           # Prints the size of the current image
    totalwidth = totalwidth + imagewidth       # Adds the current image width to the total width
    totalheight = totalheight + imageheight    # Adds the current image height to the total height

meanwidth = totalwidth // imagecount   #Calculates the average width of all images 
meanheight = totalheight // imagecount #Calculates the average height of all images 

print("Total width:", totalwidth)   # Prints the total width of all images added together
print("Total height:", totalheight) # Prints the total height of all images added together

print("Average width:", meanwidth) # Prints the average width
print("Average height:", meanheight) # Prints the average height

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)

        imgResized = img.resize((meanwidth, meanheight), Image.Resampling.LANCZOS)
        imgResized.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], " is resized")

videoname = "My_collage.avi"
os.chdir(path)
images = []
for i in os.listdir('.'):
    images.append(i)
print(images)
frame = cv2.imread(os.path.join(".", images[0]))
video = cv2.VideoWriter(videoname, 0, 1, (meanwidth, meanheight))
for i in images:
    video.write(cv2.imread(os.path.join(".", i)))
