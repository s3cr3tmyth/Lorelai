# import packages
from kmeans import KMeans
import matplotlib.pyplot as plt
import argparse
import helper
import cv2

# argument parser 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True)
ap.add_argument("-c", "--clusters", required = True, type = int)
args = vars(ap.parse_args())

# Load the image
# When the image file is read with the OpenCV function imread(), the order of colors is BGR (blue, green, red).
# Therefore, if you want to use OpenCV function, you need to convert BGR and RGB.

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)


# reshape the image
image = image.reshape((image.shape[0] * image.shape[1], 3))


# Calling the Kmeans function
k = KMeans(K=args["clusters"], max_iters=150)
labels, centroids = k.predict(image)

# build a histogram of clusters
hist = helper.centroid_histogram(labels)
# bar of the number of pixels labeled to each color
bar = helper.plot_colors(hist, centroids)
# show color pallette bar
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()

# To run
# color_kmeans.py --image images/jp.png --clusters 3
