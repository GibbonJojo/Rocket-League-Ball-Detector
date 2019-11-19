from PIL import ImageGrab
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

def process_img(img):
    # Convert the image color to gray
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #new_img = cv2.GaussianBlur(new_img, (10,11), cv2.BORDER_DEFAULT)
    # Detect edges
    new_img = cv2.Canny(new_img, threshold1=150, threshold2=350)
    return new_img

def roi(img):
    # cut out some of the picture to detect less circles
    new_img = img[250:750, 770:1200]

    return new_img


def detect_circle(img, original_img):
    # detect the circles
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.7 ,170, param2=120, minRadius=0, maxRadius=125)

    # draw the circles
    if circles is not None:
        circles = np.round(circles[0,:]).astype("int")
        for (x,y,r) in circles:
            cv2.circle(original_img[250:750, 770:1200], (x,y), r, (1,255,1), 10)
            cv2.circle(img, (x,y), r, (1,255,1), 4)

    return original_img, img

while True:
    last_time = time.time()
    # Grab the Screen and convert the list to a np array
    screen = np.array(ImageGrab.grab())

    proc_img = process_img(screen)
    roi_img = roi(proc_img)
    new_img, circle_img = detect_circle(roi_img, screen)

    cv2.imshow("Rocket League Screengrab", circle_img)

    cv2.namedWindow("RL Screen", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("RL Screen", (960,540))
    cv2.imshow("RL Screen", cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB))

    print("Loop took: ", time.time()-last_time)

    if cv2.waitKey(25) & 0xFF == ord('q'):
         cv2.destroyAllWindows()
         break
