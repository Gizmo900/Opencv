

#This Python program uses OpenCV to recognise faces. 
# It reads photos from a training dataset where each folder represents a different person,
#  converts the photos to greyscale, resizes them, and gives each person a number. 
# It detects faces and draws boxes around them, but it trains the recogniser on the whole photo,
#  including the background. 
# Finally, it tests the recogniser on a photo in the test folder and prints two values: 
#             the number of the person it thinks is the closest match and 
#             a score showing how close the match is.
# A lower score means a closer match.


# 1. Import the libraries
import cv2          # OpenCV detects and recognises faces.
import numpy as np  # NumPy converts the labels into an array for training.
import os           # Used to list folders and build file paths.

# 2. Load the face detector
face_cascade = cv2.CascadeClassifier(
    r"C:/Users/parsa/OneDrive/Desktop/Jetlearn coding/Opencv/haarcascade_frontalface_default.xml"
)  # This file contains a trained detector for front-facing faces.

# 3. Set up the training data
dataset_path = r"c:\Users\parsa\OneDrive\Desktop\Jetlearn coding\Facedatasets3"
images = []  # Stores the training photos.
labels = []  # Stores the person number for each photo.
count = 0    # The first person's label is 0.

# 4. Read and prepare each photo
for subdir in os.listdir(dataset_path):  # Each folder represents one person.
    print(count, subdir)  # Show this person's number and folder name.

    for image in os.listdir(os.path.join(dataset_path, subdir)):
        img_path = os.path.join(dataset_path, subdir, image)
        img = cv2.imread(img_path, 0)      # 0 loads the photo in greyscale.
        img = cv2.resize(img, (500, 500))  # Make every photo 500 × 500 pixels.

        # 5. Detect faces and draw boxes around them
        faces = face_cascade.detectMultiScale(
            img,
            scaleFactor=1.1,  # Look for faces at different sizes.
            minNeighbors=8    # Require several nearby detections to confirm a face.
        )
        for (x, y, w, h) in faces:  # Position, width and height of each face.
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

        # 6. Store the photo and its label
        images.append(img)    # Store the whole photo, including any boxes.
        labels.append(count)  # Photos in the same folder get the same label.

    count += 1  # Move to the next person's number after finishing this folder.

# 7. Inspect the training data
#print(images)  # Print the photos as arrays of pixel values.
#print(labels)  # Print the corresponding person numbers.

# 8. Train the face recogniser
model = cv2.face.LBPHFaceRecognizer_create()  # LBPH compares local pixel patterns.
model.train(images, np.array(labels))         # Learn from the labelled photos.

# 9. Test the recogniser on a photo of Shakira
#test1 = cv2.imread(
#    r"C:\Users\parsa\OneDrive\Desktop\Jetlearn coding\Facedatasets2\Shakira\02.jpg", 0
#)
#test1 = cv2.resize(test1, (500, 500))  # Match the training photo size.
#result = model.predict(test1)          # Find the closest match in the training data.
#print(result)  


# 9. Test the recogniser on another photo
photo_path = r"C:\Users\parsa\OneDrive\Desktop\Jetlearn coding\TestPhotos\Taylor Swift\05.jpg" # Change this to the path of the photo you want to test.
test_photo = cv2.imread(photo_path, 0)  # Load in greyscale.

if test_photo is None:
    print("Could not open the photo. Check the file path:", photo_path)
else:
    test_photo = cv2.resize(test_photo, (500, 500))   # Match the training photo size.
    person_number, distance = model.predict(test_photo)
    print("Predicted person number:", person_number)
    print("Distance:", round(distance, 2))  # Prints (predicted person number, distance). Lower means a closer match.