
from PIL import Image, ImageFilter
import colorsys
import cv2
import math
import numpy as np
import sys
import progressbar

im = Image.open(sys.argv[1])

arr = np.array(im)
hsvs = np.zeros((im.height, im.width, 3))

print("Gathering HSV values\n")

for y in progressbar.progressbar(range(im.height)):
	for x in range(im.width):
		(r, g, b) = (arr[y][x][0], arr[y][x][1], arr[y][x][2])
		(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
		hsvs[y][x][0] = h
		hsvs[y][x][1] = s
		hsvs[y][x][2] = v

print("Done fetching hsv\n")

frame = 0
for shift in progressbar.progressbar(np.arange(0, 1, 0.02)):
	im = Image.fromarray(arr)
	im.save('sky-diamonds-{:0>2d}.jpg'.format(frame))
	for y in range(im.height):
		for x in range(im.width):
			h = math.modf(hsvs[y][x][0] + shift)[0];
			(r, g, b) = colorsys.hsv_to_rgb(h, hsvs[y][x][1], hsvs[y][x][2])
			arr[y][x][0] = r
			arr[y][x][1] = g
			arr[y][x][2] = b
	frame += 1

