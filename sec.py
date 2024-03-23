import cv2
img = cv2.imread("C:/training/luffy.jpeg")
print(img)
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow(img)
cv2.imwrite('grey.jpg', gry)
cv2.imwrite('rgb.jpg',rgb)