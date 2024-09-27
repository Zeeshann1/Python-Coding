
#import numpy as np
#import cv2

#img = cv2.imread("image.png", 1)

# Draw rectangle on image
#img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 5)

#cv2.imshow('Image', img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()



import numpy as np
import cv2

# Open video capture device
cap = cv2.VideoCapture("video.mp4")

# Create a window to display the video
cv2.namedWindow('Video')

# Initial rectangle coordinates and size
x, y, w, h = 384, 0, 126, 128

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # If the video frame is not available, break the loop
    if not ret:
        break
    
    # Draw rectangle on the frame
    frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
    
    # Display the frame
    cv2.imshow('Video', frame)
    
    # Wait for a key press
    key = cv2.waitKey(30) & 0xFF
    
    # If the 'q' key is pressed, exit the loop
    if key == ord('q'):
        break
    
    # Modify the rectangle coordinates based on key presses
    if key == ord('w'):
        y -= 5
    elif key == ord('s'):
        y += 5
    elif key == ord('a'):
        x -= 5
    elif key == ord('d'):
        x += 5

# Release video capture device and close all windows
cap.release()
cv2.destroyAllWindows()


