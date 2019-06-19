import cv2, time

video = cv2.VideoCapture("random.mp4")

a = 1

while True:
    a = a + 1
    check, frame = video.read()
    # print(frame)
    # print(check)
    if check == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capturing", gray)
        key = cv2.waitKey(1)
    else:
        break
    # if key == ord('q'):
    #     break

print("Number of frames in the video: ", a)
video.release()
cv2.destroyAllWindows()



