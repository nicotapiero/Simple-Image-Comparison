from skimage.metrics import structural_similarity
import cv2
import numpy as np

import sys
import os

def compare(path1, path2):
    first = cv2.imread(path1)
    second = cv2.imread(path2)

    if first.shape != second.shape:
        # change to size of smaller one
        if first.shape[0]*first.shape[1] < second.shape[0] * second.shape[1]:
            first, second = second, first
        second = cv2.resize(second, (first.shape[1], first.shape[0]), interpolation = cv2.INTER_AREA)

    # Compute SSIM between two images
    score, diff = structural_similarity(first, second, full=True, channel_axis=2)
    return score

source_image = sys.argv[2]
path_of_images = sys.argv[1]

mx = 0
curr_best = ""

options = []

for filename in os.listdir(path_of_images):
    if filename.endswith('.jpg'):
        curr = compare(path_of_images + filename, source_image)

        options.append((curr,filename))
        # if curr > mx:
        #     mx = curr
        #     curr_best = filename


options.sort()
options.reverse()
print()
print()
print(path_of_images + options[0][1])
print("Similarity Score: {:.3f}%".format(options[0][0] * 100))

print(options[0:5])
