#!/usr/bin/python3
# -*- coding: utf-8 -*-


BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]

SIZE = 1400
ONE = 1./SIZE
EDGE = 0.05

GAMMA = 1.4

GRAINS = 10

NOISE_SCALE = 0.00001


def run(sand):
  from modules.walkers import Walkers

  walkers = []

  for i in range(2):
    walkers.append(Walkers(
      SIZE,
      EDGE,
      NOISE_SCALE
      ).run())

  while walkers:
    new_walkers = []
    for w in walkers:
      try:
        dots = next(w)
        sand.paint_strokes(dots[:-1,:], dots[1:,:], GRAINS)
      except Exception as e:
        print(e)
      else:
        new_walkers.append(w)
      walkers = new_walkers


def main():
  from sand import Sand
  from fn import Fn

  sand = Sand(SIZE)
  sand.set_bg(BACK)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  run(sand)
  name = fn.name()
  sand.write_to_png(name, GAMMA)


if __name__ == '__main__':
  main()

