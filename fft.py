import numpy as np
import cmath
import math
import random


# TODO: Create circular function

def equal(a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        diff = a[i] - b[i]
        abs_diff = round(abs(diff), 5)
        assert abs_diff == 0.0

# TODO: Get rido of np
def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    else:
        even = ifft(x[::2])  # TODO: Get rido of ::
        odd = ifft(x[1::2])  # TODO: Get rido of ::
        factor = np.exp(2j * np.pi * np.arange(N) / N)
        return np.concatenate([even + factor[:N//2] * odd,
                               even + factor[N//2:] * odd]) / 2

# TODO: Get rido of np
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    else:
        even = fft(x[::2])  # TODO: Get rido of ::
        odd = fft(x[1::2])  # TODO: Get rido of ::
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([even + factor[:N//2] * odd,
                               even + factor[N//2:] * odd])


def main(n):
    L = 2**n
    x = [random.randint(0, 1000) for _ in range(L)]
    y = fft(np.array(x))
    z = np.fft.fft(x)
    equal(y, z)
    xx = ifft(y)
    equal(x, xx)


main(6)
