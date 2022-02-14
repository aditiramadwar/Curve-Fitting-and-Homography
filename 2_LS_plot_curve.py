# @file 2_LS_plot_curve.py
# @author Aditi Ramadwar (adiram@umd.edu)
# @brief Curve fitting using the least-square method
# @date 2022-02-04
import numpy as np
import matplotlib.pyplot as plt

#### Standard Least Square ####
# The derived normal equations
# y_sum = n*a1 + a2*x_sum + a3*x_sq_sum
# x_y_sum = a1*x_sum + a2*x_sq_sum + a3*x_cb_sum
# x_sq_y_sum = a1*x_sq_sum + a2*x_cb_sum + a3*x_4_sum
def LS(x,y):
    n=len(x)
    x_sum=np.sum(x)
    x_sq = np.square(x)
    x_sq_sum = np.sum(x_sq)
    x_cb_sum = np.sum(x**3)
    x_4_sum = np.sum(x**4)
    y_sum = np.sum(y)
    x_y_sum = np.sum(x*y)
    x_sq_y_sum = np.sum(x_sq*y)
    A = np.array ([[n,x_sum,x_sq_sum],
                [x_sum, x_sq_sum, x_cb_sum],
                [x_sq_sum, x_cb_sum, x_4_sum]])
    B= np.array([[y_sum],[x_y_sum],[x_sq_y_sum]])

    A_inv = np.linalg.inv(A)
    X = np.dot(A_inv,B)
    a1=X[0]
    a2=X[1]
    a3=X[2]
    #parabola formula = ax^2 + bx + c
    y_new = a3*(x_sq) + a2*x + a1 
    return y_new

def read_file(vid_name):
    x,y=[],[]
    f= open("results/"+vid_name+".txt", "r+") 
    for l in f:
        row = l.split()
        x = np.append(x,int(row[0]))
        y = np.append(y,int(row[1]))
    return x,y
    
def process(vid_name):
    x, y = read_file(vid_name)
    y_new = LS(x, y)
    n = len(x)
    #plot best fitting curve
    plt.plot(x, y_new)
    # Adding limits on axis to replicate the image coordinate system
    plt.ylim(y_new[n-1], 0)
    plt.xlim(0, x[n-1])
    # plot data points
    plt.scatter(x, y)
    # naming the axis
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Curve for'+vid_name)
    plt.savefig("results/"+'LS_'+vid_name+'.png')
    plt.show()
#vid_name = 'Ball_travel_10fps' #Ball_travel_2_updated #Ball_travel_10fps

process('Ball_travel_10fps')
process('Ball_travel_2_updated')
