import cv

img=cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)

)
cv2.putText(
    img,
    "Earth",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (355,355,355)

)
cv2.putText(
    img,
    "mars",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (400,500,500)

)
cv2.putText(
    img,
    "Jupiter",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (400,350,400)

)


 cv2.imshow(“output”,img)
 cv2.waitKey(0)