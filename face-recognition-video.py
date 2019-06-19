# import cv2, time
#
# # Creating a cascade classifier object
# face_cascade = cv2.CascadeClassifier("C:/Python36x86x64/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("C:/Python36x86x64/Python36/Lib/site-packages/cv2/data/haarcascade_eye.xml")
#
# # Video Capture from file
# video = cv2.VideoCapture("SampleVideo_1280x720_1mb.mp4")
# # video = cv2.VideoCapture(0)
#
# # Counter for frames
# a = 1
#
# while True:
#     a = a + 1
#     check, frame = video.read()
#     if check == True:
#         # Converting the img to GrayScale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # Search the co-ordinates of the image
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5,  minSize=(30, 30))
#         for x, y, w, h in faces:
#             img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.imshow("Capturing", gray)
#         key = cv2.waitKey(1)
#     else:
#         break
#
#
#
# video.release()
# cv2.destroyAllWindows()


import cv2
import sys


faceCascade = cv2.CascadeClassifier("C:/Python36x86x64/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture("random.mp4")
# num_frames = 1
# while True:
#     num_frames += 1
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()
#     print(ret)
#     if ret == True:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # Search the co-ordinates of the image
#         # faces = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
#         # # faces = faceCascade.detectMultiScale(
#         # #     gray,
#         # #     scaleFactor=1.1,
#         # #     minNeighbors=5
#         # # )
#         #
#         # # Draw a rectangle around the faces
#         # for (x, y, w, h) in faces:
#         #     # video_captureS = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         #     img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
#         # Display the resulting frame
#         # cv2.imshow('Video', img)
#         cv2.imshow("Capturing", gray)
#     else:
#         break

scale_factor = 1.2
min_neighbors = 3
min_size = (50, 50)
webcam= False #if working with video file then make it 'False'

a = 1

while True:
    a = a + 1
    check, frame = video_capture.read()
    # print(frame)
    # print(check)
    if check == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # faces = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors
                                         )
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        print("Frame Counter: ", a)
    else:
        break
    # if key == ord('q'):
    #     break

print("Number of frames in the video: ", a)
video_capture.release()
cv2.destroyAllWindows()

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
