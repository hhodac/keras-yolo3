# Introduction
This folder contains codes & experiments continuing the master thesis works. The purpose is to complete the idea of analyzing the biases of object detection (YOLOv3), together with additional attempt to publish a paper and gain a PhD position at the University of Melbourne, under the instruction of Dr.Kris Ehinger.

# Previous works review
In the results of the master thesis works, there were two significant issues relevant to the biases of the dataset itself, as well as the problem of our cropping methodology.

The first issue was about the uneven distribution of object classes. When we sorted the object class by its count, there was a significant gap in the number of objects counted between the top and the bottom object class in the list. As a result, when applying the cropping method, object classes at the bottom of this list encountered two major issues:
1. Initially, the number of object in these classes was insufficient to output a decent distribution for analysis. 
2. As if the initial number of objects in these classes met our expected threshold, the number of qualified objects left after applying the cropping method, again, still could not output a decent distribution for analysis.

The second issue, as mentioned above, was about the cropping methodology we used. In short, there were two major issues we need to overcome:
1. The cropping method was too naive, which resulted in cropped images with weird shape as it would never exist in practice.
2. The qualitative criteria after cropping images was strict, so the number of qualified images were insufficient to output a decent distribution for analysis.

Therefore, in the following proposal methods, we will try to overcome the above issues and re-examine the result with new methods:
* Method 1: ignores individual object class and produces as many qualified images as possible.
* Method 2: generates new samples from the cropping.

## Method 1: ignores individual object class
In this method, our definition for a qualified image is simple:
* Newly cropped images are able to contain images in four corners.
* Raw image -> img_crop_temp (3x3) has obj in the middle area -> img_crop_1, _2, _3, _4 have obj in one of the corner respectively.

## Method 2: generate new samples
If the cropped images exceeds the image's edge, we can try to pad it to achieve required resolution. This act might result in unrealistic situation of the object position, however, we can temporarily ignore it here.

The padding ideas are:
* if object is not overlapping with one of the corner -> copy that object to four corner -> apply prediction & analyse
* pad with either white, black or random pixel value
* pad with opposite side of the image (imagining rolling the image like a tube)
* crop random other area that meet our resolution threshold and put the object into corresponding corner.

In this method, we simply ignore the relationship of object's locations in practice.