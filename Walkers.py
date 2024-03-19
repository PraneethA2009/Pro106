import cv2

# Create our body classifier
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Initiate video capture for video file
pedestrians = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = walking.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Walkers', frame)

    if cv2.waitKey(1) == 32:
        break

cap.release()
cv2.destroyAllWindows()