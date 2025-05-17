from PIL import Image
import numpy as np

def convolve(pix, kernel):
    height, width = pix.shape
    kernelHeight, kernelWidth = kernel.shape
    padHeight = kernelHeight // 2
    padWidth = kernelWidth // 2

    padImage = np.pad(pix, ((padHeight, padHeight), (padWidth, padWidth)), mode='edge')
    resultPix = np.zeros_like(pix, dtype=np.float64)

    for x in range(height):
        for y in range(width):
            resultPix[x, y] = np.sum(padImage[x:x + kernelHeight, y:y + kernelWidth] * kernel)
    return resultPix


def kayyali(pix):
    Gx = np.array([[-6, 0, 6],
                   [ 0, 0, 0],
                   [-6, 0, 6]])

    Gy = np.array([[-6, 0, -6],
                   [ 0, 0,  0],
                   [ 6, 0,  6]])

    gradX = convolve(pix, Gx)
    gradY = convolve(pix, Gy)
    gradient = np.abs(gradX) + np.abs(gradY)

    return gradX, gradY, gradient


def normalize(gradient):
    gradNorm = (gradient - gradient.min()) / (gradient.max() - gradient.min()) * 255
    return gradNorm.astype(np.uint8)

def binarize(gradient, threshold, resultFilename):
    gradBinary = (gradient > threshold).astype(np.uint8) * 255
    Image.fromarray(gradBinary).save(resultFilename)
    print(f"The binarized gradient matrix of the image {resultFilename.split('/')[-1][:-10] + '.bmp'} is preserved...\n")