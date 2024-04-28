#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:39:01 2024

@author: westonlarhette
"""

""" Lab 8 Ex 4: Plot the trajectory of a 2D Random Walk"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 42)

num_steps = 500
x_step = rng.random(num_steps) > 0.5
y_step = rng.random(num_steps) > 0.5


x_step = 2*x_step - 1
y_step = 2*y_step - 1


x_position = np.cumsum(x_step)
y_position = np.cumsum(y_step)


plt.figure()
plt.plot(x_position,y_position)
plt.xlabel('x-position')
plt.ylabel('y-position')
plt.axis("equal")
plt.title('2D Random Walk')

plt.show()
