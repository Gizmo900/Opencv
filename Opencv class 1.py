






import cv2          # This lets us use OpenCV (for working with images)
import os           # This helps work with files (not used much here)

import cv2          # (Repeated import – not needed again, but doesn't break anything)

# -------------------- LOAD AND SHOW ORIGINAL IMAGE --------------------

# Load the image from your computer
img = cv2.imread(r'C:\Users\parsa\Desktop\Jetlearn coding\Opencv\monster.png')

# Check if the image loaded correctly
if img is None:
    print("Error: Could not load image. Check path.")   # Show error if file not found
else:
    cv2.imshow('My original picture', img)   # Show the image in a window
    cv2.waitKey(0)                          # Wait until you press a key
    cv2.destroyAllWindows()                 # Close the window

# -------------------- SHOW IMAGE IN GREYSCALE --------------------

# Load the same image but in greyscale (black & white)
image2 = cv2.imread(r'C:\Users\parsa\Desktop\Jetlearn coding\Opencv\monster.png', 0)

cv2.imshow("original in greyscale", image2)  # Show greyscale image
cv2.waitKey(0)                              # Wait for key press
cv2.destroyAllWindows()                     # Close window

# -------------------- SPLIT IMAGE INTO COLOURS --------------------

# Load image in colour
image3 = cv2.imread(r'C:\Users\parsa\Desktop\Jetlearn coding\Opencv\monster.png', 1)

# Split the image into Blue, Green, and Red parts
b, g, r = cv2.split(image3)

# Show BLUE part of the image
cv2.imshow("original in blue saturation", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show GREEN part of the image
cv2.imshow("original in green saturation", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show RED part of the image
cv2.imshow("original in red saturation", r)
cv2.waitKey(0)
cv2.destroyAllWindows()












