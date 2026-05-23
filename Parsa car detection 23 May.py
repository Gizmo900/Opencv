# This program opens a video, reads it frame by frame, converts each frame to black and white,
# detects cars using the cars.xml classifier, draws rectangles around detected cars,
# and shows the result as a video. Press q on the keyboard to stop the program.

import cv2 # Import OpenCV, a library used for image and video processing.

# Open the video file from the computer.
original_video = cv2.VideoCapture(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Video\carvideo1.mp4")

# Load the trained car detection classifier file.
car_detection_classifier = cv2.CascadeClassifier(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\Video\cars.xml")

# Check if the video file opened successfully.
if not original_video.isOpened():
    print("Error: Could not open the video file.") # Show an error message if the video cannot be opened.

# Keep running while the video is open.
while original_video.isOpened():
    # Read one frame from the video.
    ret, current_frame = original_video.read()
  
    # If ret is False, it means there are no more frames to read.
    if not ret:
        break # Stop the loop when the video finishes.

    # Convert the current frame from colour to grayscale.
    gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the grayscale frame.
    cas = car_detection_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=1)

    # Go through each detected car.
    for (x, y, w, h) in cas:

        # Draw a blue rectangle around the detected car
        cv2.rectangle(current_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show the video frame with detected cars.
    cv2.imshow("Car detection video", current_frame)

    # Wait for 1 millisecond and check if the user presses the 'q' key.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break # Stop the video if the user presses 'q'.

# Release the video file from memory.
original_video.release()

# Close all OpenCV windows.
cv2.destroyAllWindows()