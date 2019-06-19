import cv2

# Read the image through opencv, here 1 defines the coloured image and 0 means the GreyScale/BnW img
img = cv2.imread("dummy.jpg", 0)

print(type(img))
exit()

# To display, we call the imshow func and give the image a name and itself
cv2.imshow("Background", img)

# The wait key param 0 defines the image is up until a key is pressed other any given milliseconds
cv2.waitKey(0)

# To destroy all the windows once the waitKey is called over
cv2.destroyAllWindows()

# To print the shape of the image i.e. along with its channel (3 for coloured and 1 for GreyScale)
# print(img.shape)


# To resize the image (but it isn't symmetrical)
resized_img = cv2.resize(img, (300, 300))
cv2.imshow("Resized_Background", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# To resize the image symmetrically
resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Symmetrically_Resized_Background", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# To resize the image symmetrically (increase in size)
resized_img = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))
cv2.imshow("Symmetrically_Doubled_Resized_Background", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

