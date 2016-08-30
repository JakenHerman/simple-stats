from __future__ import division

ages = [35, 52, 45, 70, 24, 43, 68, 77, 45]

def minimum():
    minimum = ages[0]
    for age in ages:
        minimum = age if (age < minimum) else minimum
    return minimum

def maximum():
    maximum = ages[0]
    for age in ages:
        maximum = age if (age > maximum) else maximum
    return maximum

def mean(stats):
    mean = 0
    for stat in stats:
        mean += stat
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

# median function declaration
def median(stats):
    sort(stats)
    half = round(len(stats)/2)
    if len(stats) % 2 == 0:
        return mean([stats[half-1], stats[half]])
    return stats[half]

        