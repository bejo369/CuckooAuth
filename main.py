import cv2
import numpy as np
import sys
from lib.utils import *
from optparse import OptionParser

np.set_printoptions(threshold=sys.maxsize)  # display numpy array in full


# convert img to binry 
def con_bin_img(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    ret, img_th = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
    return img_th


# display binary image
def display_img(binary_img):
    for i in range(len(binary_img)):
        for j in range(len(binary_img[i])):
            if binary_img[i][j] == 1:
                binary_img[i][j] = 255

    cv2.imshow("my test binary img", binary_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def div_block(blk_size, bin_img):
    blocks = []
    for y in range(0, bin_img.shape[0], blk_size):
        for x in range(0, bin_img.shape[1], blk_size):
            blk = bin_img[y:y + blk_size, x:x + blk_size]
            blocks.append(blk)
    return blocks


def main():
    parser = OptionParser()
    parser.add_option("-i", "--image", dest="img",
                      help="input an image")
    parser.add_option("-d", "--display", dest="display", action="store_true", default=False,
                      help="display image")
    parser.add_option("-p", "--print_bin", dest="print_bin", action="store_true", default=False,
                      help="display binary")
    parser.add_option("-k", "--key", dest="key", help="Enter User Key")
    (options, args) = parser.parse_args()
    # convert test img to binary and display
    img = options.img
    bin_img = con_bin_img(img)

    if options.print_bin:
        print(bin_img)
    if options.display:
        display_img(bin_img)
    print(div_block(200, bin_img.reshape(1, bin_img.size)))


main()
