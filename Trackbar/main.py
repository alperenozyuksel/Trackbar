import cv2
import numpy as np

def nothing(x):
    pass

can = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("canvas")

cv2.createTrackbar("R","canvas", 0,255, nothing)
cv2.createTrackbar("G","canvas", 0,255, nothing)
cv2.createTrackbar("B","canvas", 0,255, nothing)
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch,"canvas", 0,1, nothing)

while True:
    cv2.imshow("canvas", can)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "canvas")
    g = cv2.getTrackbarPos("G", "canvas")  # ALINAN DEGERLERI KAYDETME
    b = cv2.getTrackbarPos("B", "canvas")
    s = cv2.getTrackbarPos(switch,"canvas")

    if s == 0:
        can[:] == [0,0,0]
    if s == 1:
        can[:] = [b,g,r]



cv2.destroyAllWindows()








