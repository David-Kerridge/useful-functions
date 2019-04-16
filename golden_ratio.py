# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:14:40 2013

@author: djk
"""
# Continued fraction to compute golden ratio

import math
level = 10
ans   = 1.0

for i in range (0 , level ):
    ans = 1.0 + (1.0 / ans )
    
phi = 0.5 * (1 + math . sqrt (5) )
print (' Actual value of PHI is : ', phi)
print (' Approximation is : ', ans) 