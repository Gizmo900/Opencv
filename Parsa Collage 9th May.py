
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

# Loops through each file in the folder
for file in os.listdir('.'):

    # Checks if the file is an image is an image file
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):

        # Opens the image file
        img = Image.open(os.path.join(path, file))

        # Gets width and height of the image
        width, height = img.size

        # Prints the original width and height of the image
        print(width, height)

        # Resizes the image to the average width and the average height
        imgResized = img.resize((meanwidth, meanheight), Image.Resampling.LANCZOS)

        # Saves the resized image as a JPEG with good quality
        imgResized.save(file, 'JPEG', quality = 95)

        # Prints the image name and confirms it has been resized
        print(img.filename.split('\\')[-1], "is resized")

# Sets the name of the output video file
videoname = "My_collage.avi"

# Changes the current working folder to the image folder
os.chdir(path)

# Creates an empty list to store image file names
images = []

# Loops through all files in the folder and add their names to the list
for i in os.listdir('.'):
    images.append(i)

# Prints the list of image files
print(images)

# Reads the first image from the list 
frame = cv2.imread(os.path.join(".", images[0]))

# Creates a video writer object 
# 0 means default codec, 1 means 1 frame per second,
# and (meanwidth, meanheight) is the video frame size
video = cv2.VideoWriter(videoname, 0, 1, (meanwidth, meanheight))

# Loops through each image in the list
for i in images:

    # Reads each image and writes it as a frame in the video
    video.write(cv2.imread(os.path.join(".", i)))