import cv2 as cv
import numpy as np

img = cv.imread('obje_50.jpeg', 0)

#size of image
rows,cols = np.shape(img)

x = np.zeros_like(img)
y = 255*np.ones_like(img)

#thresholding a image
thresh = np.where(img>200, y, x)

#creating a screen of size equal to image where labeling of objects to be done
screen = thresh

#object number
obj = 1

while True:
    #gave first white pixel as the pixel of object 1
    for i in range(rows):
        for j in range(cols):
            if screen[i][j] == 255:
                screen[i][j] = obj
                break
        if screen[i][j] == obj:
            break

    #gave neighbourhood white pixels labelling
    for i in range(rows):
        for j in range(cols):
            try:
                if screen[i][j] == 255:
                    if screen[i+1][j] == obj or screen[i+1][j+1] == obj or screen[i][j+1] == obj or screen[i-1][j+1] == obj or screen[i-1][j] == obj or screen[i-1][j-1] == obj or screen[i][j-1] == obj or screen[i+1][j-1] == obj:
                        screen[i][j] = obj
                    else:
                        continue
            except:
                continue

    if 255 not in screen:
        break

    obj = obj + 1

obj = 1


while obj in screen:
    for i in range(rows):
        for j in range(cols):
            if screen[i][j] != obj and screen[i][j] != 0:
                if screen[i + 1][j] == obj or screen[i + 1][j + 1] == obj or screen[i][j + 1] == obj or screen[i - 1][j + 1] == obj or screen[i - 1][j] == obj or screen[i - 1][j - 1] == obj or screen[i][j - 1] == obj or screen[i + 1][j - 1] == obj:
                    screen[i][j] = obj

    obj = obj +1

#mapping objects to hue value
screen_hue = np.uint8(179*screen/np.max(screen))
blank_ch = 255*np.ones_like(screen_hue)
labeled_img = cv.merge([screen_hue, blank_ch, blank_ch])

#convert BGR for display
labeled_img = cv.cvtColor(labeled_img, cv.COLOR_HSV2BGR)
#set background to black
labeled_img[screen_hue==0] = 0
cv.imshow('labeled_img', labeled_img)

cv.waitKey(0)
cv.destroyAllWindows()
