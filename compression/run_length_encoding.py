import numpy as np

class Rle:
    def __init__(self):
        pass

    def encode_image(self, binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        rle_code = []
        count = 0
        last_pix = -1
        flatten_image = binary_image.flatten()

        for pixel in flatten_image:
            if last_pix == -1:
                last_pix = pixel
                count += 1
            else:
                if last_pix != pixel:
                    rle_code.append((count, last_pix))
                    last_pix = pixel
                    count = 1
                else:
                    if count < (2**8) - 1:
                        count+=1
                    else:
                        rle_code.append((count, last_pix))
                        last_pix=pixel
                        count = 1

        rle_code.append((count, last_pix))
        
        return np.array(rle_code)


    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        shape = [height, width]
        decoded_image = list()

        for code in rle_code:
            count = code[0]
            pixel = code[1]
            decoded_image.extend([pixel] * count)

        original_image = np.array(decoded_image).reshape(shape)
        return original_image