import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


def create_harmonic(length, points_count, frequency):
    x = np.arange(0, length, length/points_count)
    y = np.cos(math.pi * 2 * frequency * x)

    return x, y


def create_digital(length, points_count, frequency):
    x, y = create_harmonic(length, points_count, frequency)

    for i in range((len(y))):
        if y[i] > 0:
            y[i] = 1
        if y[i] <= 0:
            y[i] = 0

    return x, y


def create_spectrum(y):
    yf = fft(y)
    yf = yf[1: len(yf) // 2]
    return abs(yf)


def show(x, y):

    plt.subplot(221)
    plt.title('signal:')
    plt.plot(x, y)
    plt.grid(True)

    plt.subplot(222)
    plt.title('spectrum:')
    plt.plot(create_spectrum(y))
    plt.grid(True)

    plt.show()
