
#OpenCV is a tool in coding that helps a computer see and understand pictures and videos
# This program uses OpenCV to load an image and show it in different ways:
# It opens the original image.
# It shows the same image in black and white (greyscale).
# It splits the image into blue, green, and red parts and shows each one separately.

import cv2   # This lets us use openCV (for working with images)
import os    # This helps work with files (not used much here)
import numpy as np

#--------------------LOAD AND SHOW ORIGINAL IMAGE----------------------

#Loa the image from your computer
img = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\frontartgreen.jpg")

# Check if the image loaded correctly
if img is None:
    print("Error: Could not load image. Check path") # Shows error if file not found
else:
    cv2.imshow('My original picture', img) # Show the image in a window
    cv2.waitKey(0)                         # Wait until you press a key
    cv2.destroyAllWindows()                # Close the window


resizedimage = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\frontartgreen.jpg", 1)
resizedimage = cv2.resize(resizedimage, (250, 250))

cv2.imshow('Small image', resizedimage) # Show the image in a window
cv2.waitKey(0)                         # Wait until you press a key
cv2.destroyAllWindows()    



#--------------------SHOW IMAGE IN GREYSCALE-------------------

# Load the same image but in greyscale (Black & White)
image2 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\frontartgreen.jpg", 0)

cv2.imshow("original in greyscale", image2) # Show greyscale image
cv2.waitKey(0)                              # Wait for key press
cv2.destroyAllWindows()                     # Close window

#--------------------SPLIT IMAGE INTO COLOURS--------------------

# Load image in colour (It loads an image from your computer in full colour and stores it 
# in the variable image3.)
image3 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\frontartgreen.jpg", 1)

# Split the image into Blue, Green, and Red parts
b, g, r = cv2.split(image3)

# Show blue part of the image
cv2.imshow("original in blue saturation", b) 
cv2.waitKey(0)                              
cv2.destroyAllWindows()                     


# Show green part of the image
cv2.imshow("original in green saturation", g) 
cv2.waitKey(0)                              
cv2.destroyAllWindows() 

# Show red part of the image
cv2.imshow("original in red saturation", r) 
cv2.waitKey(0)                              
cv2.destroyAllWindows() 

image4 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\frontartgreen.jpg", 1)
b, g, r = cv2.split(image4)
zeroarray = np.zeros_like(b)
blueimage = cv2.merge([b, zeroarray, zeroarray])
redimage = cv2.merge([zeroarray, zeroarray,r])
greenimage = cv2.merge([zeroarray, g, zeroarray])


cv2.imshow("blue saturated image", blueimage) 
cv2.waitKey(0)                              
cv2.destroyAllWindows() 

cv2.imshow("green saturated image", greenimage) 
cv2.waitKey(0)                              
cv2.destroyAllWindows() 

cv2.imshow("red saturated image", redimage) 
cv2.waitKey(0)                              
cv2.destroyAllWindows() 