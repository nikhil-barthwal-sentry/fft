import numpy as np
import cmath
import math
import random
from typing import List


def equal(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if round(abs(a[i] - b[i]), 5) != 0.0:
            return False
    return True


def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    else:
        even = ifft(x[::2])
        odd = ifft(x[1::2])
        factor = np.exp(2j * np.pi * np.arange(N) / N)
        return np.concatenate([even + factor[:N//2] * odd,
                               even + factor[N//2:] * odd]) / 2


class FFT:

    def __init__(self, indexes: List[int], inverse: bool):
        self.indexes: List[int] = indexes
        self.N: int = len(indexes)
        if self.N > 1:
            assert self.N % 2 == 0
            self.even = FFT(indexes[::2])
            self.odd = FFT(indexes[1::2])
            self.factor = []
            for i in range(self.N):
                self.factor.append(np.exp(-2j * np.pi * i / self.N))

    def fft(self, x):
        if self.N <= 1:
            return [x[self.indexes[0]]]

        assert self.N % 2 == 0
        even = self.even.fft(x)
        odd = self.odd.fft(x)
        half = self.N // 2
        assert len(even) == half
        assert len(odd) == half
        r1 = []
        r2 = []
        for i in range(half):
            r1.append(even[i] + self.factor[i] * odd[i])
            r2.append(even[i] + self.factor[half + i] * odd[i])
        return r1 + r2


def main(n):
    indexes = list(range(2**n))
    f = FFT(indexes)
    x = [random.randint(0, 1000) for _ in indexes]
    y = f.fft(x)
    z = np.fft.fft(x)
    assert equal(y, z)
    xx = ifft(y)
    assert equal(x, xx)


main(6)
