
#This program uses OpenCV to process two images. It loads Bulbasaur and Charmander images, resizes them,
#  and subtracts one from the other to highlight their differences. 
# It also applies two types of blurring (Gaussian and median) to smooth the images and then displays the results on the screen.



import cv2  # Import OpenCV library for image processing

# Load two images from file paths
image1 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Bulbasaur.jpg")
image2 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Charmander.png")

# Read and resize first image to 250x250 pixels
resizedimage1 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Bulbasaur.jpg")
resizedimage1 = cv2.resize(resizedimage1, (250, 250))

# Read and resize second image to 250x250 pixels
resizedimage2 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Charmander.png ")
resizedimage2 = cv2.resize(resizedimage2, (250, 250))

# Subtract the second image from the first image (pixel-wise comparison)
subtractimage = cv2.subtract(resizedimage1, resizedimage2)

# Display the subtracted image
cv2.imshow("subtracted image", subtractimage)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()  # Close the window

# Apply Gaussian Blur to the first image (smooths and reduces noise)
GaussionBlurimage = cv2.GaussianBlur(image1, (7, 7), 0)

# Display blurred image
cv2.imshow("Blurred image", GaussionBlurimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply Median Blur to the second image (removes noise while keeping edges)
Medianblurredimage = cv2.medianBlur(image2, 35)

# Display median blurred image
cv2.imshow("Medianblurr image", Medianblurredimage)
cv2.waitKey(0)
cv2.destroyAllWindows()













