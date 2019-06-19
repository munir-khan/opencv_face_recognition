import cv2

# Creating a cascade classifier object
face_cascade = cv2.CascadeClassifier("C:/Python36x86x64/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:/Python36x86x64/Python36/Lib/site-packages/cv2/data/haarcascade_eye.xml")

# Reading the Image
img = cv2.imread("celebs.jpg")
# img = cv2.imread("celebs_2.jpg")

# Converting the img to GrayScale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.35, minNeighbors=4)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
    # roi_gray = gray_img[y:y + h, x:x + w]
    # roi_color = img[y:y + h, x:x + w]
    # eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=5)
    # for (ex, ey, ew, eh) in eyes:
    #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)

# resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))
print(type(img))
cv2.imshow("Face_Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


