import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "sun",
    (20, 300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "mercury",
    (100, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "venus",
    (200, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "earth",
    (300, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "mars",
    (390, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "jupiter",
    (500, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "saturn",
    (800, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "uranus",
    (1000, 150),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "neptune",
    (1121, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.imshow("probablyNotAWindow", img)

cv2.waitKey(0)

cv2.imwrite("named_Solar_System.jpg", img)