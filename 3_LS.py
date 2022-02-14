import matplotlib.pyplot as plt
import numpy as np
import csv

file = open('data/ENPM673_hw1_linear_regression_dataset.csv')
csvreader = csv.reader(file)
header = next(csvreader)
age=[]
salary=[]

for row in csvreader:
    age = np.append(age,int(row[0]))
    salary = np.append(salary,float(row[6]))
file.close()
n = len(age)
A = np.array([[n,       np.sum(age)],
            [np.sum(age), np.sum(age**2)]])

B = np.array([[np.sum(salary)], [np.sum(age*salary)]])

A_inv = np.linalg.inv(A)
# X = A^-1 * B
X = np.dot(A_inv, B)
a=X[0] # c
b=X[1] # m
# line formula = bx + a = y
curve = b*age + a
plt.plot(age, curve,'r')
# plot data points
plt.scatter(age, salary)
plt.xlabel('age')
plt.ylabel('salary')
plt.savefig("results/3_LS.png")
plt.show()
