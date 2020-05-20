## This is the abstract class that the students should implement

from modesEnum import Modes
import numpy as np
import cv2


class ImageModel():

    """
    A class that represents the ImageModel
    """

    def __init__(self):
        pass

    def __init__(self, imgPath: str):
        self.imgPath = imgPath
        ###
        # ALL the following properties should be assigned correctly after reading imgPath
        ###
        self.imgByte = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        self.dft = np.fft.fft2(self.imgByte)
        self.real = np.real(self.dft)
        self.imaginary = np.imag(self.dft)
        fshift = np.fft.fftshift(self.dft)
        self.magnitude = 20*np.log(np.abs(fshift))
        self.phase = np.angle(self.dft)

    def mixing(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float, mode: 'Modes') -> np.ndarray:
        array1, array2 = self.mix_func(mode, self, imageToBeMixed, magnitudeOrRealRatio, phaesOrImaginaryRatio)
        return self.update_photo(mode, array1, array2)

    def mix_func(self, mode: 'Modes', img1: 'ImageModel', img2: 'ImageModel', ratio1: 'float', ratio2: float):
        if mode == Modes.magnitudeAndPhase:
            mix1 = np.add((abs(img1.dft) * ratio1), (abs(img2.dft) * (1 - ratio1)))
            mix2 = np.add((img1.phase * ratio2), (img2.phase * (1 - ratio2)))
            mix2 = np.exp(1j * mix2)
            return mix1, mix2
        elif mode == Modes.realAndImaginary:
            mix1 = np.add((img1.real * ratio1), (img2.real * (1 - ratio1)))
            mix2 = np.add((img1.imaginary * ratio2), (img2.imaginary * (1 - ratio2)))
            mix2 = (1j * mix2)
            return mix1, mix2
        elif mode == Modes.magnitudeAndUniformPhase:
            mix1 = np.add((abs(img1.dft) * ratio1), (abs(img2.dft) * (1 - ratio1)))
            mix2 = np.zeros(img1.phase.shape)
            mix2 = np.exp(1j * mix2)
            return mix1, mix2
        elif mode == Modes.uniformMagnitudeAndPhase:
            mix1 = np.ones(img1.magnitude.shape)
            mix2 = np.add((img1.phase * ratio2), (img2.phase * (1 - ratio2)))
            mix2 = np.exp(1j * mix2)
            return mix1, mix2
        elif mode == Modes.uniformMagnitudeAndUniformPhase:
            mix1 = np.ones(img1.magnitude.shape)
            mix2 = np.zeros(img2.phase.shape)
            mix2 = np.exp(1j * mix2)
            return mix1, mix2

    # function which return output that will be displayed
    def update_photo(self, mode: 'Modes', array1: 'np.ndarray', array2: 'np.ndarray') -> np.ndarray:
        if array1 is None or array2 is None:
            output = np.array([[]])
            return output
        else:
            if mode == Modes.magnitudeAndPhase or mode == Modes.magnitudeAndUniformPhase or mode == Modes.uniformMagnitudeAndPhase:
                output = np.copy(array2 * array1)
                output = np.real((np.fft.ifft2(output)))
                return output
            elif mode == Modes.uniformMagnitudeAndUniformPhase:
                output = np.copy(array2 * array1)
                output = np.real((np.fft.ifft2(output)))
                return output
            elif mode == Modes.realAndImaginary:
                output = np.add(array1, array2)
                output = np.real(np.fft.ifft2(output))
                return output
