import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

def obj(x,y,b=1):
    return -b*(x**2 + y**2)

# def obj(x,y,a,b,c,d):
#     z = (x**2/a**2)+(y**2/b**2)
#     return -(((x - b) / a) ** 2 + ((y - d) / c) ** 2) + 1.0


##### setup

init = np.asarray([[-6,-6],[-5.07,-5.61],[-5.61,-5.08]])






def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# Z = obj(X,Y,a,b,c,d)
Z = obj(X,Y,b)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')


############################################
def results(num_variables, init):
    result = np.zeros(num_variables+1)

    for i in range(0,num_variables+1):
        x = init[i][0]
        y = init[i][1]
        result[i] = obj(x,y)
    return result


result_array = results(2,init)
#############################################
def find_worst(result_array):
    worst = np.argmin(result_array)
    return worst
current_worst = find_worst(result_array)

############################################

def midpoint(num_variables,current_worst,parameter_array):
    midPoint = np.zeros(num_variables)
    for j in range(0,num_variables):
             midPoint[j] = np.sum(parameter_array[:num_variables+1,j])/num_variables # number of rows = numvariables +1, you do this for each column
    return midPoint

parameter_centroid = midpoint(2,init)
#############################################

def find_worst(result_array):
    worst = np.argmin(result_array)
    return worst
current_worst = find_worst(result_array)

#####################################

def newpoint(worst,centroid,parameter_array):
    alpha =1
    old_x = init[worst][0]
    old_y = init[worst][1]

    centroid_x = centroid[0]
    centroid_y = centroid[1]

    new_x = centroid_x + alpha*(centroid_x-old_x)
    print(new_x)
    new_y = centroid_y + alpha*(centroid_y-old_y)
    print(new_y)
    parameter_array[worst][0] = new_x
    parameter_array[worst][1] = new_y

    return parameter_array

init = newpoint(current_worst,parameter_centroid,init)
