from PIL import Image, ImageOps
import numpy as np
from contour import convolve, kayyali, normalize, binarize


files = ['cat', 'hogwarts', 'map', 'text_flower', 'x_ray']

for name in files[4:]:
    filename = f"Pictures/{name}/{name}Grayscale.bmp"
    resultFilename = f"Pictures/{name}/{name}"

    resultFiles = dict(Gx=f"{resultFilename}Gx.bmp", Gy=f"{resultFilename}Gy.bmp", G=f"{resultFilename}G.bmp", binary=f"{resultFilename}Binary.bmp")

    img = Image.open(filename)
    pix = np.array(img)
    gradientX, gradientY, gradient = kayyali(pix)

    gradXNorm = normalize(gradientX)
    gradYNorm = normalize(gradientY)
    gradientNorm = normalize(gradient)

    Image.fromarray(gradXNorm).save(resultFiles['Gx'])
    Image.fromarray(gradYNorm).save(resultFiles['Gy'])
    Image.fromarray(gradientNorm).save(resultFiles['G'])
    print(f"The gradient matrices of the {name + '.bmp'} image are preserved...")

    threshold = 40
    binary_gradient = binarize(gradientNorm, threshold, resultFiles['binary'])
