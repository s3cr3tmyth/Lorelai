# Lorelai (Personal Project)

## Idea:

The idea of project came about when I was watching video on youtube about Radiohead's artwork for Kid-A. I have always been fascinated by album artworks and meaning behind it. As a life long Fleet Foxes fan, I decided to do dive deep into their artwork style.

Fleet Foxes Self titled album cover features a segment of Pieter Bruegel‘s painting ‘Netherlandish Proverbs’, which is fascinating in itself. So, I decided to  create colour palettes in python (for data visualisation) that were based on colours present in the album covers of Fleet Foxes. 

Project name stems from song named 'Lorelai' from Fleet Foxes Helplessness Blues album.

While braistorming ways to automatically generate the colour palettes from the album covers so that a colour palette could be created from any given image, I realised that this could be only done in an unsupervised manner. 

Clustering algorithms such as K-Means segment features (colors in this case) from data (image) based on similar characterstics (distance)

There are various python libraies present which can do this for you. (e.g colorgram which is a Python library that lets you extract colors from images)
But I decided to do it from scratch using OpenCV and numpy. 

## Steps :

#### 1) Get High resolution version of album art possible

I used this wonderful site created by Ben Dodson* which lets you download high-res version of artwork from itunes.

#### 2) Convert images to vectors

When Loading the image with the OpenCV function imread(), the order of colors is BGR (blue, green, red).
Therefore, if you want to use OpenCV function, you need to convert BGR and RGB.

#### 3) Write Kmeans from scratch

Implement K-means from scratch using numpy

#### 4) Write helper function to count the number of pixels that belong to each cluster and generate histogram

#### 5) Write another helper function to generate barplot displaying how many pixels were assigned to each cluster based on the output of the histogram

#### 6) Tie everything together and viola!


## To run:

1) Clone this repo

2) Run lorelai.py by passing two arguments image path and number of clusetrs. 

(Change the number of clusters for more numnber of palettes)

```
lorelai.py --image artwork/*.png --clusters 5
```


## Results 

![GitHub Logo](/results/1111.png)
![GitHub Logo](/results/2222.png)
![GitHub Logo](/results/3333.png)
![GitHub Logo](/results/4444.png)
![GitHub Logo](/results/5555.png)


## Refrernces:

#### 1) https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/ (For the helper functions)

#### 2) https://www.nme.com/news/music/fleet-foxes-31-1324001

#### 3) https://bendodson.com/projects/itunes-artwork-finder/
