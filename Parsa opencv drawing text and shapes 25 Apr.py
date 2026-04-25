

# This program uses the OpenCV library to load three images from my computer and draw different shapes and text on them.
#  It first draws a blue line on the first image, then draws a red rectangle and a filled green rectangle on the second image,
#  and a circle on the first image again. Finally, it writes the text “Hello, I am learning OpenCV” on the third image. 
# Each modified image is displayed in a window one at a time, waiting for a key press before closing and moving to the next.


import cv2
import numpy as np

# -------- Load Images --------
image1 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Minions.jpg")
image2 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Panda.jpg")
image3 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\LionKing.jpg")

#-------1. Draw a line -------
startpoint = (0,0)
endpoint = (200,200)
linecolor = (255, 0, 0)
thickness = 5

line_image = cv2.line(image1.copy(), startpoint, endpoint, linecolor, thickness)
cv2.imshow("Line image", line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-----------2. Draw a normal rectangle----------
rectanglecolor = (0, 0, 255) #Red

rectangle_image = cv2.rectangle(image2.copy(), startpoint, endpoint, rectanglecolor, thickness)
cv2.imshow("Rectangle", rectangle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------3. Draw a FILLED rectangle--------
# Use thickness  = -1 for filled
filled_rectangle = cv2.rectangle(image2.copy(), (50, 50), (250, 350), (0, 255, 0), -1)

                                                                                       #image2.copy() → makes a duplicate so the original image isn’t changed
                                                                                       #(50, 50) → top-left corner of the rectangle
                                                                                       #(250, 350) → bottom-right corner
                                                                                       #(0, 255, 0) → green color (in BGR format)
                                                                                       #-1 → fills the rectangle instead of just drawing the border

cv2.imshow("Filled rectangle", filled_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

#------------------4. Draw a circle------------------
center = (200, 200)
radius = 100
circle_color = (255, 255, 0) #Cyan

circle_image = cv2.circle(image1.copy(), center, radius, circle_color, thickness)

cv2.imshow("Circle", circle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------5. Add text --------------
text = "Hello, I am learning OpenCV"
position = (50, 250)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
text_color = (0, 255, 255) #Yellow
text_thickness = 2

text_image = image3.copy()
cv2.putText(text_image, text, position, font, font_scale, text_color, text_thickness)

cv2.imshow("Text on image", text_image)
cv2.waitKey(0)
cv2.destroyAllWindows()