#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:20:45 2024

@author: westonlarhette
"""
""" Lab 8 Ex. 1: taxicab distance measurement"""

import numpy as np

def distance(point1, point2, metric = "taxi"):
    """
    Return distance in miles between point1 & point2
    If metric is 'taxi' or omitted, use taxicab (straightline) metric
    Otherwise use euclidean distance
    point1 = (x1,y1). List, tuple, or numpy array
    point2 = (x2,y2). List, tuple or numpy array
    metric : TYPE, optional
        DESCRIPTION. The default is "taxi".
    """
    if metric == 'taxi':
        distance = abs(point2[0] - point1[0]) + abs(point2[1]-point1[1])
    else:
        distance = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    
    return distance

