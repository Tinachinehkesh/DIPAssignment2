import numpy as np
import cv2
import math
import dip

class ShapeCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Implement the blob coloring algorithm
        takes as input:
        image: binary image
        return: a list/dict of regions
        """

        regions = dict()
        R = np.zeros((image.shape[0], image.shape[1]), dtype=int)
        k = 1
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] == 255 and image[i][j-1] == 0 and image[i-1][j] == 0:
                    R[i][j] = k
                    regions[k] = [[i, j]]
                    k = k + 1
                elif image[i][j] == 255 and image[i][j-1] == 0 and image[i-1][j] == 255:
                    R[i][j] = R[i-1][j]
                    regions[R[i-1][j]].append([i, j])
                elif image[i][j] == 255 and image[i][j-1] == 255 and image[i-1][j] == 0:
                    R[i][j] = R[i][j-1]
                    regions[R[i][j-1]].append([i, j])
                elif image[i][j] == 255 and image[i][j-1] == 255 and image[i-1][j] == 255:
                    R[i][j] = R[i-1][j]
                    regions[R[i-1][j]].append([i, j])
                    if R[i][j-1] != R[i-1][j]:
                        regions[R[i-1][j]].extend(regions[R[i][j-1]])
                        regions[R[i][j-1]] = []

        return regions

    def identify_shapes(self, region):
        """Compute shape features area and centroid, and shape
        Ignore shapes smaller than 10 pixels in area.
        takes as input
        region: a list/dict of pixels in a region
        returns: shapes, a data structure with centroid, area, and shape (c, s, r, or e) for each region
        c - circle, s - squares, r - rectangle, and e - ellipse
        """

        # Please print your shape statistics to stdout, one line for each shape
        # Region: <region_no>, centroid: <centroid>, area: <shape area>, shape: <shape type>
        # Example: Region: 871, centroid: (969.11, 51.11), area: 707, shape: c

        shapes = []
        count = 0
        for k in region.keys():
            if len(region[k]) > 10:
                area = len(region[k])
                pixels = region[k]
                x = 0
                y = 0
                count += 1
                for i in pixels:
                    x += i[1]
                    y += i[0]
                x /= len(region[k])
                y /= len(region[k])
                centroid_val = (int(x), int(y))

                min_x = min(pixels, key=lambda p: p[0])[0]
                max_x = max(pixels, key=lambda p: p[0])[0]
                min_y = min(pixels, key=lambda p: p[1])[1]
                max_y = max(pixels, key=lambda p: p[1])[1]

                # Calculate width and height
                width = max_x - min_x
                height = max_y - min_y

                # Identify shape
                shape = ""
                symmetric_threshold = 0.05 * (width + height) / 2
                if abs(width - height) <= symmetric_threshold:
                    if abs(width - 2 * math.sqrt(area/math.pi)) <= symmetric_threshold:
                        shape = "circle"
                    else:
                        shape = "square"
                else:
                    area_hole = abs(width * height - area)
                    if area_hole <= 0.05 * (width * height):
                        shape = "rectangle"
                    else:
                        shape = "ellipse"

                print(f"Region: {count}, centroid: ({centroid_val[0]:.2f}, {centroid_val[1]:.2f}), area: {area}, shape: {shape[0]}")
                shapes.append([count, area, centroid_val, shape])

        return shapes

    def count_shapes(self, shapes_data):
        """Compute the count of shapes using the shapes data returned from identify shapes function
           takes as input
           shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
           returns: a dictionary with count of each shape
           Example return value: {'circles': 21, 'ellipses': 25, 'rectangles': 31, 'squares': 23}
           """
        c = 0
        e = 0
        r = 0
        s = 0
        for elem in shapes_data:
            if elem[3] == "square":
                s += 1
            elif elem[3] == "circle":
                c += 1
            elif elem[3] == "rectangle":
                r += 1
            elif elem[3] == "ellipse":
                e += 1
        return {"circles": c, "ellipses": e, "rectangles": r, "squares": s}

    def mark_image_regions(self, image, shapes_data):
        """Creates a new image with computed stats for each shape
        Make a copy of the image on which you can write text.
        takes as input
        image: binary image
        shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
        returns: image marked with center and shape_type"""

        img = image.copy()
        for data in shapes_data:
            shape = data[3][0]
            centroid = data[2]
            font = dip.FONT_HERSHEY_SIMPLEX
            color = (0, 0, 0)
            img = cv2.putText(img, shape, (centroid[0], centroid[1]), font, 1, color, 2, dip.LINE_AA)

        return img

