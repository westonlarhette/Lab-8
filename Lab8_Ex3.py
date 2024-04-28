#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:27:58 2024

@author: westonlarhette
"""

""" Lab 8 Ex. 3: Simulating coin flips & returning total # of heads after 100 flips"""

import numpy as np

rng = np.random.default_rng()
num_flips = 100

samples = rng.random(num_flips)
flips = samples < 0.5

num_heads = sum(flips)