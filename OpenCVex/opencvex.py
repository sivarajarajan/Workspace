# Sample of open cv

# Loading the image
import numpy as np
from matplotlib import pyplot as plt

import cv2
import sys


class processImage():
    def __init__(self, pic):
        self.pic = pic
        self.img = 0

    def readColor(self):
        self.img = cv2.imread(self.pic, cv2.IMREAD_COLOR)

        # cv2.line(self.img, (0, 0), (50, 50), (0, 0, 255), 3)
        # cv2.rectangle(self.img, (150, 200), (350, 350), (0, 255, 0), 3)
        # cv2.circle(self.img, (20, 100), 20, (120, 120, 120), 3)  # Circle with border
        # cv2.circle(self.img, (20, 150), 20, (180, 0, 180), -1)  # Circle with filled color
        #
        # points = np.array([[50, 10], [50, 20], [80, 30], [30, 40]], np.int32)
        # cv2.polylines(self.img, [points], True, (100, 100, 0), 3)
        #
        # fnt = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        # cv2.putText(self.img, "LENOVO", (100, 50), fnt, 2, (80, 80, 80), 2, cv2.LINE_AA)

    def greyImage(self, ):
        # Reading the image in greyscale
        self.img = cv2.imread(self.pic, 0)


    def displayEdge(self):
        self.edge = cv2.Canny(self.img, 100, 500)
        plt.subplot(121)
        plt.imshow(self.img, cmap="gray")
        plt.subplot(122)
        plt.imshow(self.edge, cmap="gray")

        plt.show()


    def displayImage(self, img=None, usecv2=True):
        if usecv2:
            cv2.imshow("OpenCV", self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            #print self.img
            plt.imshow(self.img, cmap='gray', interpolation='bicubic')
            plt.plot([50, 100], [50, 400], "c", linewidth=3)
            plt.show()


def main():

    if len(sys.argv) > 1:
        print "Processing image :", sys.argv[1]

    pi = processImage()
    pi.greyImage()
    #pi.displayImage()
    pi.displayEdge()

if __name__ == "__main__":
    main()