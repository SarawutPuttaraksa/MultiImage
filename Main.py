import cv2
import numpy as np
from MultiImage import stackImages

def Thres(imgThres):
    #imgBlur = cv2.GaussianBlur(imgThres, (5, 5), 3)
    imgHsv = cv2.cvtColor(imgThres, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("H Min", "HSV")
    h_max = cv2.getTrackbarPos("H Max", "HSV")
    s_min = cv2.getTrackbarPos("S Min", "HSV")
    s_max = cv2.getTrackbarPos("S Max", "HSV")
    v_min = cv2.getTrackbarPos("V Min", "HSV")
    v_max = cv2.getTrackbarPos("V Max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    print([h_min, h_max, s_min, s_max, v_min, v_max])
    #kernel = np.ones((5, 5))
    #imgDil = cv2.dilate(mask, kernel, iterations=1)
    return mask

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.resizeWindow('image', 640, 300)
cv2.createTrackbar('H Min', 'image', 0, 255, nothing)
cv2.createTrackbar('H Max', 'image', 255, 255, nothing)
cv2.createTrackbar('S Min', 'image', 110, 255, nothing)
cv2.createTrackbar('S Max', 'image', 255, 255, nothing)
cv2.createTrackbar('V Min', 'image', 169, 255, nothing)
cv2.createTrackbar('V Max', 'image', 255, 255, nothing)
cv2.createTrackbar("Area", "image", 100, 50000, nothing)


def Colororange (img, x):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([x[0], x[2], x[4]])
    upper = np.array([x[1], x[3], x[5]])

    mask = cv2.inRange(imgHsv, lower, upper)
    return mask

def contourscolor (imgcon, text):

    contours, hieracrhy = cv2.findContours(imgcon, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    numO = 0
    numG = 0
    numR = 0
    numB = 0
    numP = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        x, y, w, h = cv2.boundingRect(approx)

        areaMin = cv2.getTrackbarPos("Area", "image")

        if area >= areaMin:
            if text == 'o':
                numO += 1
                cv2.drawContours(img, contours, -1, (100, 100, 255), 2)
                shape(len(approx), numO, [x, y], (100, 100, 255))

            if text == 'r':
                numR += 1
                cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
                shape(len(approx), numR, [x, y], (0, 0, 255))

            if text == 'g':
                numG += 1
                cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
                shape(len(approx), numG, [x, y], (0, 255, 0))

            if text == 'b':
                numB += 1
                cv2.drawContours(img, contours, -1, (171, 138, 70), 2)
                shape(len(approx), numB, [x, y], (171, 138, 70))

            if text == 'p':
                numP += 1
                cv2.drawContours(img, contours, -1, (255, 0, 150), 2)
                shape(len(approx), numP, [x, y], (255, 0, 150))

    if text == 'o':
        cv2.putText(img, "Orange:{:.0f}".format(numO), (0, 370), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (100, 100, 255), 2)
    if text == 'r':
        cv2.putText(img, "Red:{:.0f}".format(numR), (0, 390), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (0, 0, 255), 2)
    if text == 'g':
        cv2.putText(img, "Green:{:.0f}".format(numG), (0, 410), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (0, 255, 0), 2)
    if text == 'b':
        cv2.putText(img, "Blue:{:.0f}".format(numB), (0, 430), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (171, 138, 70), 2)
    if text == 'p':
        cv2.putText(img, "Purple:{:.0f}".format(numP), (0, 450), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (255, 0, 150), 2)

def shape(app, num, location, color):
    if app == 3:
        cv2.putText(img, "triangle:{:.0f}".format(num), (location[0], location[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                    color, 2)
    elif app == 4:
        cv2.putText(img, "rectangle:{:.0f}".format(num), (location[0], location[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                    color, 2)
    elif app == 5:
        cv2.putText(img, "pentagon:{:.0f}".format(num), (location[0], location[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                    color, 2)
    elif app > 5:
        cv2.putText(img, "circle:{:.0f}".format(num), (location[0], location[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                    color, 2)


path = r'C:\Users\nonza\PycharmProjects\pythonProject\cap\Largest-object-in-an-image-Python-OpenCV.png'
wigth, hight = 640, 460

Orange = [7, 62, 118, 255, 2, 255]
Red = [128, 179, 209, 233, 0, 255]
Blue = [0, 179, 233, 255, 0, 255]
Purple = [107, 173, 99, 255, 0, 255]
Green = [66, 75, 138, 255, 5, 255]

while True:
    img = cv2.imread(path)
    img = cv2.resize(img, (wigth, hight))

    imgOrange = Colororange(img, Orange)
    imgRed = Colororange(img, Red)
    imgBlue = Colororange(img, Blue)
    imgPurple = Colororange(img, Purple)
    imgGreen = Colororange(img, Green)

    contourscolor(imgOrange, 'o')
    contourscolor(imgRed, 'r')
    contourscolor(imgBlue, 'b')
    contourscolor(imgPurple, 'p')
    contourscolor(imgGreen, 'g')

    imgStack_Shape = stackImages(0.4, ([img, imgOrange, imgRed],
                                       [imgBlue, imgPurple, imgGreen]))
    cv2.imshow('img', imgStack_Shape)
    cv2.waitKey(1)

