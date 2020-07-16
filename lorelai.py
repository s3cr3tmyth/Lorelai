# import the necessary packages
from kmeans import KMeans
import matplotlib.pyplot as plt
import argparse
import helper
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int,
	help = "# of clusters")
args = vars(ap.parse_args())
# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)


# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))


# cluster the pixel intensities
# k = KMeans(n_clusters = args["clusters"])
# clt.fit(image)
k = KMeans(K=args["clusters"], max_iters=150)
labels, centroids = k.predict(image)

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = helper.centroid_histogram(labels)
bar = helper.plot_colors(hist, centroids)
# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()


# color_kmeans.py --image images/jp.png --clusters 3