from datetime import datetime
from requests import HTTPError
from requests import ConnectionError
from pandas import *
from numpy import *
from matplotlib import pyplot as plt
from itertools import groupby

hockeyPoints = read_csv("http://ds101.seangoggins.net/hockeyPoints.csv", 
    header=None, )

#hockeyPoints = read_csv("http://ds101.seangoggins.net/BostonMarathon2013Times-Seconds.csv", 
#    header=None, )

### Look at 40 bins
#plt.hist(hockeyPoints[0], bins=45)

### Look at 200 bins
plt.hist(hockeyPoints[0], bins=50)

### Look at 500 bins
#plt.hist(hockeyPoints[0], bins=500)

plt.show()

# This will plot a line graph
# plt.plot(hockeyPoints[0])
