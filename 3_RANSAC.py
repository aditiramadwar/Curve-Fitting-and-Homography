import matplotlib.pyplot as plt
import numpy as np
import random
import csv
def LS(x,y):
    n = len(x)
    den = np.sum(np.power(x,2)) - (np.sum(x)**2)/n #n * np.sum(np.power(x,2)) - np.sum(x)**2
    num = np.sum(np.dot(x,y)) - (np.sum(y)*np.sum(x))/n #n * np.sum(np.dot(x,y)) - np.sum(y)*np.sum(x) 
    m = num/den
    c = np.sum(y) - m*np.sum(x)
    return m, c

file = open('data/ENPM673_hw1_linear_regression_dataset.csv')
csvreader = csv.reader(file)
header = next(csvreader)
age = np.array([])
salary = np.array([])
for row in csvreader:
    age = np.append(age,int(row[0]))
    salary = np.append(salary,float(row[6]))
file.close()

er_th = np.std(salary)/2
final_inlier = -np.inf
prob = 0.95
e = 0.5
# calculate number of iterations
itr = int(np.log(1-prob)/np.log(1-(1-e)**2))

for i in range(itr):
    # select two random points
    idx = random.sample(range(len(age)-1), 2)
    x = age[idx]
    y = salary[idx]

    m, c = LS(x,y)

    inlier = 0
    for j in range(len(age)):
        y_temp = age[j]*m + c
        er = abs(y_temp - salary[j])
        if er < er_th:
            inlier += 1
    if (inlier > final_inlier):
        final_inlier = inlier
        final_x = x
        final_y = y
        final = [m, c]
y_max = final[0]*max(age)+final[1]
y_min = final[0]*min(age)+final[1]
plt.plot([max(age),min(age)], [y_max,y_min], "r")
plt.scatter(age, salary)
plt.xlabel('age')
plt.ylabel('salary')
# plt.savefig('results/RANSAC.png')
plt.show()
