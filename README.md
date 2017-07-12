# Travelling-Salesman-Problem

Probably the easiest way to solve this problem is to test all possible permutations of a given array. Not the most effective way because there are n! possible solutions, where n is the number of cities. In future, I'm going to improve this way, because right now I'm using python library called random, which randomly shuffles the order of cities in an array. However, it often repeats itself because there is no function checking whether the array has been tested so far.

# UPDATE

Added a function checking for used solutions. Improves reliabilty, as no path may ever be used again. 
