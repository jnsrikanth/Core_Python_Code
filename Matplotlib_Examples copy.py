import matplotlib

#Example 1: This is a very simple example related to a basic 2-axis
# plotting of a data set.

#Importing pyplot
from matplotlib import pyplot as plt

#Plotting to our canvas
plt.plot([1,2,3],[4,5,1])

#Showing what we plotted
plt.show()

#Example 2: Another Example of maplotlib with x and y axis
from matplotlib import pyplot as plt

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

#Example 3: Another Example of ggplot

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

# can plot specifically, after just showing the defaults:
plt.plot(x,y,linewidth=5)
plt.plot(x2,y2,linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


#Example of a Bar Chart

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]


plt.bar(x, y, align='center')

plt.bar(x2, y2, color='g', align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

#Example of a Scatter Chart

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.scatter(x, y)#, align='center')

plt.scatter(x2, y2, color='g')#, align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

#Example of a Python plot with data loaded from a CSV file.
# Data loaded into the csv file is as below (Separate CSV file provided)
# 1,5
# 2,7
# 3,8
# 4,3
# 5,5
# 6,6
# 7,3
# 8,7
# 9,2
# 10,12
# 11,5
# 12,7
# 13,2
# 14,6
# 15,9
# 16,2

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')
    
    
    unpack=True,
        delimiter = ',')

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()





