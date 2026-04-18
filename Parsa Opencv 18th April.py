

# This program uses OpenCV to process two images. It loads Bulbasaur and Charmander images, resizes them,
# and performs subtraction, addition, multiplication, and division to compare them.
# It also applies Gaussian and median blurring and displays all results.

import cv2
import numpy as np  # Needed for multiply and divide

# Load two images from file paths
image1 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Bulbasaur.jpg")
image2 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Charmander.png")

# Resize both images to 250x250 pixels
resizedimage1 = cv2.resize(image1, (250, 250))
resizedimage2 = cv2.resize(image2, (250, 250))  

# -------- Image Arithmetic Operations --------

#Subtract
subtractimage = cv2.subtract(resizedimage1, resizedimage2)
cv2.imshow("Subtracted Image", subtractimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Add
addimage = cv2.add(resizedimage1, resizedimage2)
cv2.imshow("Added Image", addimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Multiply (convert to float to avoid overflow, then scale back)
multiplyimage = cv2.multiply(resizedimage1.astype(float), resizedimage2.astype(float))    # Why float? Images are normally stored as uint8 (0–255).
                                                                                          # if you multiply two uint8 numbers, they can overflow (go above 255)       
                                                                                          #Example:         
                                                                                          #200 × 200 = 40000 → too big for uint8, but OK for float.
multiplyimage = np.clip(multiplyimage / 255, 0, 255).astype('uint8')                       #astype() changes the data type of the image.
                                                                                          #astype(float) → allows safe math operations
                                                                                          #astype('uint8') → converts back to normal image format so it can be displayed

cv2.imshow("Multiplied Image", multiplyimage)               #multiplies pixel values  
                                                                #Areas where both images are bright → become very bright
                                                                #Areas where one image is dark → become darker
                                                                #Overall effect:
                                                                #Looks darker and more contrasted
                                                                #Only common features stand out
cv2.waitKey(0)
cv2.destroyAllWindows()

# Divide (avoid division by zero)
divideimage = cv2.divide(resizedimage1, resizedimage2 + 1)  #+1 Prevents division by zero
cv2.imshow("Divided Image", divideimage)                               #It divides pixel values of one image by the other.
                                                                       #Where image2 is dark → result becomes bright
                                                                       # Where image2 is bright → result becomes darker
cv2.waitKey(0)
cv2.destroyAllWindows()

# -------- Blurring --------

# Gaussian Blur (smooths image)
GaussianBlurimage = cv2.GaussianBlur(image1, (7, 7), 0)
cv2.imshow("Gaussian Blurred Image", GaussianBlurimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Median Blur (removes noise)
Medianblurredimage = cv2.medianBlur(image2, 35)
cv2.imshow("Median Blurred Image", Medianblurredimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()