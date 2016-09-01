#imports
from __future__ import division
import math

#our sample data
ages = [35, 52, 45, 70, 24, 43, 68, 77, 45, 28]

#minimum function declaration
def minimum(stats):
    minimum = stats[0]
    for stat in stats:
        #determine if the entity is the smallest in the list
        minimum = stat if (stat < minimum) else minimum
    return minimum

#maximum function declaration
def maximum(stats):
    maximum = stats[0]
    for stat in stats:
        #determine if the entity is the largest in the list
        maximum = stat if (stat > maximum) else maximum
    return maximum

#mean function declaration
def mean(stats):
    mean = 0
    for stat in stats:
        #sum each entity in stats list
        mean += stat
    #divide by the length of stats list to obtain mean    
    mean /= len(stats)
    return mean
        
# selection sort declaration
def sort(stats):
    for i in reversed(range(len(stats))):
        # Find the index of max item in stats[:i+1].
        m = 0
        for j in range(1, i + 1):
            if stats[j] > stats[m]:
                m = j
        stats[i], stats[m] = stats[m], stats[i]
    return stats

# mode function declaration
def mode(stats):
    m = max(list(map(stats.count, stats)))
    #returns a list, as there may be more than one mode
    return list(set(filter(lambda i: stats.count(i) == m, stats)))

#standard deviation function declaration
def standard_deviation(stats):
    #returns square root of variance return
    return  "{0:.3f}".format((math.sqrt(float(variance(ages)))))

#variance function declaration
def variance(stats):
    #absolute value distance from mean, squared
    sum = 0
    for stat in stats:
        sum += abs(stat - mean(stats))**2
    #divided by n numbers in stats list
    return "{0:.2f}".format(sum/(len(stats)-1))

# median function declaration
def median(stats):
    sort(stats)
    half = round(len(stats)/2)
    if len(stats) % 2 == 0:
        #if even, return mean of middle 2 entities.
        return mean([stats[half-1], stats[half]])
    #if odd, return middle entity
    return stats[half]

#range function declaration
def range(stats):
    #return maximum value entity with the minimum 
    #value entity subtracted from it
    return maximum(stats) - minimum(stats)
