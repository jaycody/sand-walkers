#!/usr/bin/python3

from numpy.random import random
from numpy import ones
from numpy import zeros
from numpy import cumsum
from numpy import column_stack
from numpy import linspace

class Walkers():
  def __init__(self, size, edge, noise_scale, num):

    self.size = size
    self.edge = edge
    self.noise_scale = noise_scale
    self.n = num

    self.one = 1.0/size

    # self.n = int(size*(1.0-2*edge))

    self.speed_scale = self.one*self.noise_scale

    x = ones(self.n, 'float')*0.5
    y = linspace(edge, 1.0-edge, self.n)
    self._walkers = column_stack((x, y))
    self._speed = zeros(self.n, 'float')

  def run(self, steps=1000000000):

    for i in range(steps):

      self._speed[:] += cumsum((1.0-2.0*random(self.n)))*self.speed_scale
      self._walkers[:, 0] += self._speed

      if any(self._walkers[:,0]>1.0-self.edge) or \
          any(self._walkers[:,0]<self.edge):
        return

      yield self._walkers

