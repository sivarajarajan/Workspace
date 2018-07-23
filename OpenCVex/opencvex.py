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

    def cannyEdges(self):
        # Find the values more than 0
        self.edge = cv2.Canny(self.img, 100, 500)
        indices = np.where(self.edge != 0)
        coordinates = zip(indices[0], indices[1])

        print "Coordinates :", coordinates

def main():

    if len(sys.argv) > 1:
        print "Processing image :", sys.argv[1]

    pi = processImage("fb.png")
    pi.greyImage()
    # pi.displayImage()
    # pi.displayEdge()
    pi.cannyEdges()


if __name__ == "__main__":
    main()