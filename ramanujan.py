# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:06:11 2017

@author: djk

Ramanujan problem. If there are n houses in a street numbered consecutively
1,2 ...n and one in number p, find possible values of n and p such that the 
sum of the house numbers less than p is equal to the sum of the numbers greater
 than p.(Where n is betwwen 50 and 500 was in the question posed.)
 
 Transferred to GitHub 14 April 2019
"""

import numpy as np

# Brute force approach using 2p^2 = n^2 + n
#
for n in range(1, 10001):
    p = np.sqrt((n*n+n)/2)
    if( (np.abs(p-np.floor(p)) < 10**(-6)) or 
        (np.abs(p-np.ceil(p))) < 10**(-6)):
        print(n, p)
#
# Solutions are n = (8, 49, 288, 1681, 9800); p = (6, 35, 204, 1189, 6930)
#

#
# Continued fraction for sqrt(2)
#
top = 1
bot = 2
levels = 20

a = np.zeros(levels)
b = np.zeros(levels)

for i in range(levels):
    a[i] = 3*bot + top
    b[i] = a[i] - bot
    top  = bot
    bot  = b[i]

print('Convergents are:')
for i in range(levels):
    print(a[i].astype(int), '/', b[i].astype(int), a[i]/b[i])

# And solve the 'houses problem' via (2n+1) = C[i], and 2p = A[i] 
# (Pell's equation)
#
for i in range(levels):
    if int(b[i]) % 2 == 0:
        print('n = ', int((a[i]-1)/2), 'p = ', int(b[i]/2))
    
# This gives the values of n and p when p is an integer

# In the language of Davenport C/A are successive convergents to sqrt(2) i.e.
# rational approximations.

# Here 7/5 is the result C[0]/A[0], then C[1]/A[1] = 17/12 etc
# (In the full continued fraction the first two convergents are 1/1 and 3/2, 
# this program starts computations at the third convergent 7/5.)

for i in range(10):
    j = i+1
    print(5**j, (5**j)%11)


(0.25).as_integer_ratio()
from fractions import Fraction
Fraction(0.25)
str(Fraction(0.25))
Fraction(0.185).limit_denominator()

for f in (0.25, 0.5, 1.25, 3.0):
    print (f.as_integer_ratio())
    print (repr(Fraction(f)), Fraction(f)) 
    
