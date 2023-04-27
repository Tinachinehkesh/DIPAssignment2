import numpy as np

class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = np.zeros(256, dtype=int)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                hist[image[i][j]] += 1

        return hist

    def find_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold assuming that the input histogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value
        Note: Use the iterative method to calculate the histogram. Do not use the Otsu's method
        Write your code to compute the optimal threshold method.
        This should be implemented using the iterative algorithm discussed in class (See Week 4, Lecture 7, slide 42
        on teams). Do not implement the Otsu's thresholding method. No points are awarded for Otsu's method.
        """

        # Initialize threshold to 0
        threshold = 0

        # Calculate the total number of pixels in the histogram
        total_pixels = sum(hist)

        # Calculate the initial mean values for the two classes
        class1_mean = 0
        class2_mean = sum([i * hist[i] for i in range(len(hist))]) / total_pixels

        # Iterate until the threshold converges
        while True:
        # Calculate the new threshold
            new_threshold = (class1_mean + class2_mean) / 2

            # Calculate the new class means
            class1_mean = sum([i * hist[i] for i in range(int(new_threshold))]) / sum(hist[:int(new_threshold)])
            class2_mean = sum([i * hist[i] for i in range(int(new_threshold), len(hist))]) / sum(hist[int(new_threshold):])

            # Check if the threshold has converged
            if abs(threshold - new_threshold) < 0.5:
                break

            # Update the threshold
            threshold = new_threshold

        return threshold

    def binarize(self, image, threshold):
        """Comptues the binary image of the input image based on histogram analysis and thresholding
        takes as input
        image: a grey scale image
        threshold: to binarize the greyscale image
        returns: a binary image"""

        hist = self.compute_histogram(image)
        thresh = self.find_threshold(hist)

        # Copying image in order not to modify the original image
        bin_image = image.copy()

        # If the pixel value is more than threshold, replace it with 255, otherwise replace it with 0.
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if bin_image[i][j] < thresh:
                    bin_image[i][j] = 0
                else:
                    bin_image[i][j] = 255

        return bin_image


