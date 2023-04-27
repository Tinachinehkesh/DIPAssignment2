# Digital Image Processing 
Assignment #2 (Shape Counting)
Due: Thu 03/21/23 11:59 PM

__________________________________________________________________________________________________________________
Objective 1: The input image contains objects of four geometric shapes: circle, square, rectangle, and ellipse. The shapes have a brighter intensity compared to the background. The objective of the assignment is to count the total number of each geometric shape in the image by performing binary image processing. The overall steps are 
1. Copmute the histogram
2. Compute optimal threshold
2. Create binary image
3. Perform blob-coloring
4. For each region, compute area, centroid, and shape (circle, square, rectangle, or ellipse)
5. Count the number of circles, number of squares, number of rectangles, and number of ellipses.
6. Mark the center of each region with a label (c for circle, r for rectangle, s for square, and e for ellipse)

Objective 2: Perform compression using run-length encoding and decoding of a binary image. 

__________________________________________________________________________________________________________________

1. (70 Pts) Shape Counting: 

 	a. (15 Pts) Write a program to binarize a gray-level image based on the assumption that the image has a bimodal histogram.  Determine the optimal threshold required to binarize the image. Your code should report both the binarized image and the optimal threshold value. Also assume that background is darker than foreground objects in the input gray-level image.
	- Starter code available in directory region_analysis/
	- region_analysis/binary_image.py:
		- compute_histogram: write your code to compute the histogram in this function, If you return a list it will automatically save the graph in output folder 
		- find_threshold: Write your code to compute the optimal threshold. This should be implemented using the iterative algorithm discussed in class (See Week 4, Lecture 7, slide 42 on teams). Do not implment the Otsu's thresholding method. No points are awarded for Otsu's method.  
		- binarize: write your code to threshold the input image to create a binary image here. This function should return a binary image which will automatically be saved in output folder. For visualization one can use intensity value of 255 instead of 1 in the binary image. That way the objects appear white over black background
	- Any output images or files will be saved to "output" folder
  
 	b. (30 Pts) Write a program to perform blob-coloring. The input to your code should be a binary image (0's, and 255's) and the output should be a list of objects or regions in the image. 
	- region_analysis/shape_counting.py:
    	- blob_coloring: write your code for blob coloring here, takes as input a binary image and returns a list/dictionary of objects or regions.
	- Any output images will be saved to "output" folder
  
	c. (15 Pts) Ignore shapes smaller than 10 pixels in area generate a report of the remaining regions (region Number, Centroid, Area, and Shape).
   - region_analysis/shape_counting.py:
        - identify_shapes: write your code for computing the statistics of each object/region, i.e area and location (centroid) here, and the shape (c for circle, s for square, r for rectancle, and e for ellipse). Print out the statistics to stdout (using print function; print one row for each region).
          - Note: You can make the following assumptions:
            - The vertical side of the squares and rectangles are parallel to the image X-axis (row). The other side should be parallel to the Y-axis 
            - The Major and minor axis are either parallel or perpendicular to the image axis. 
            - i.e. None of the shapes are rotated.
   - Any output images will be saved to "output" folder
   
   d. (5 Pts) Accumulate the statistics to count the different shapes in the image. Count the total number of circles, squares, rectangles, and ellipses, respectively. 
   - region_analysis/shape_counting.py:
   	  - count_shapes: write your code for calculating the number of circles, number of squares, number of rectangles, and number of circles. 
   - Any output images will be saved to "output" folder 

   e. (5 Pts) Generate a labelled image with the shapes marked with the type at the center of each shape. 
   - region_analysis/shape_counting.py:
      - mark_image_regions: write your code to create a final labeled image. The final image should include a single character (c, s, r, or e) representing the shape of each region at the centroid of each shape. Please see sample output below. To write text on an image, **you are allowed to use the function putText() in dip.py**.

![Alt text](results.jpg?raw=true "Sample output")

2. (30 Pts) Image Compression:

	Write a code to compress a binary image using Run length Encoding. 
	- Starter code is available in directory Compression/
	- Compression/run_length_encoding.py
		- encode_image: Write your code to compute run length code for the binary image. The input to your function will be a binary image (0's and 255's) and output ia a run length code.
		- decode_image: Write your code to recover binary image from run length code returned by encode_image funtion. The input of the function is run length code, height and width of the binary image The output of the function is the binary image recosntructed from run length code.
	- Any output image or files must be saved to "output/Compression" Folder
	 
____________________________________________________________________________________________________________________

**Note:**
We are **restricted from importing cv2, numpy, stats and other third party libraries,** 
with the only exception of math, importing math library is allowed (import math).

While you can import it for testing purposes, the final submission should not contain the following statements.
- import cv2
- import numpy
- import numpy as np
- import stats
- etc...

The essential functions for the assignment are available in dip module one can import using the following statement
```
import dip
from dip import *
```
The following functions are available

```commandline
from cv2 import namedWindow, imshow, waitKey, imwrite, imread, putText
from cv2 import FONT_HERSHEY_SIMPLEX, LINE_AA
from cv2 import ellipse, rectangle, circle

from numpy import zeros, ones, array, shape, arange
from numpy import random
from numpy import min, max
from numpy import uint8
from numpy import inf
from numpy.fft import fft2

import matplotlib
import matplotlib.pyplot as plt
```

*Assigments that contain any files that import these libraries will not be graded.* 
*Assigments that modify the dip.py file will not be graded.*
		

How to Run your code?

  - Usage: 
	>./dip_hw2_shapes.py

	(or)
	
	> pyhon dip_hw2_shapes.py
  - if you get an error "ImportError: No module named matplotlib". You can install it using the command 
	> pip install matplotlib (or)
	> python -m pip install matplotlib
  - Please make sure your code runs when you run the above command from prompt
  - Any output images or files must be saved to "output/" folder
   
  
PS. Files not to be changed: requirements.txt and jenkinsfile directory 

----------------------

Please make sure that your code is running without errors on Jenkins CI/CD.

1. Region Counting - 70 Pts. 
2. Compression     - 30 Pts.

    Total          - 100 Pts.
_______________________________________________________________________________________________________________________

<sub><sup>License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston.
This software is property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author
This software is intended to be used by students of the digital image processing course offered at University of Houston.
The contents are not to be reproduced and shared with anyone with out the permission of the author.
The contents are not to be posted on any online public hosting websites without the permission of the author.
The software is cloned and is available to the students for the duration of the course.
At the end of the semester, the Github organization is reset and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.</sub></sup>
