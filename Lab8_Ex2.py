#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:58:22 2024

@author: westonlarhette
"""

""" Lab 8 Ex. 2: Vector Rotation"""
# Provide initial vector as tuple or list
import numpy as np
def rotate_vector(r,theta):
    r = np.array([x1,y2])
    matrix = np.array([[np.cos(theta), np.sin(theta)],[-np.sin(theta),np.cos(theta)]])
    r_rotated = np.dot(matrix,r)
    return r_rotated 