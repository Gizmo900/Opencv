
import cv2
import numpy as np

image1 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Bulbasaur.jpg")
image2 = cv2.imread(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Charmander.png")

borderimage1 = cv2.copyMakeBorder(image1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 255, 255))
cv2.imshow("bordered image", borderimage1)
cv2.waitKey(0)
cv2.destroyAllWindows()

borderimage2 = cv2.copyMakeBorder(image1, 25, 25, 25, 25, cv2.BORDER_CONSTANT, value=(0, 255, 255))
cv2.imshow("bordered image", borderimage1)
cv2.waitKey(0)
cv2.destroyAllWindows()

reflectiveborder = cv2.copyMakeBorder(image1, 40, 40, 40, 40, cv2.BORDER_REFLECT, value=(0, 255, 255))
cv2.imshow("Reflective image", reflectiveborder)
cv2.waitKey(0)
cv2.destroyAllWindows()

erodem = np.ones((5, 5), np.uint8)
erosionimage2 = cv2.erode(image1, erodem)
cv2.imshow("Erosion image", erosionimage2)
cv2.waitKey(0)
cv2.destroyAllWindows()

