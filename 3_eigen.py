# @file 3_csv.py
# @author Aditi Ramadwar (adiram@umd.edu)
# @brief Covariance and eigen vectors
# @date 2022-02-05
import matplotlib.pyplot as plt
import numpy as np
import csv

file = open('data/ENPM673_hw1_linear_regression_dataset.csv')
csvreader = csv.reader(file)
header = next(csvreader)
age_og=[]
salary_og=[]
for row in csvreader:
    age_og=np.append(age_og,int(row[0]))
    salary_og=np.append(salary_og,float(row[6]))
file.close()

# Normalized the data
age = (age_og - np.min(age_og)) / (np.max(age_og) - np.min(age_og))
salary = (salary_og - np.min(salary_og)) / (np.max(salary_og) - np.min(salary_og))

age_sum = np.sum(age)
sal_sum = np.sum(salary)
mean_age = np.mean(age)
mean_sal = np.mean(salary)

cov_x_y = (np.sum((age-mean_age)*(salary-mean_sal)))/(age_og.size-1)
var_age = np.sum((age-mean_age)**2)/(age_og.size-1)
var_sal = np.sum((salary-mean_sal)**2)/(age_og.size-1)

covMatrix = [[var_age, cov_x_y],
             [cov_x_y, var_sal]]
# print("Covariance:", covMatrix)

eigen_values, eigen_vectors = np.linalg.eig(covMatrix)

eig_vec1 = eigen_vectors[:,0]
eig_vec2 = eigen_vectors[:,1]

plt.quiver(np.mean(age_og),np.mean(salary_og), (eig_vec1[0]*(np.max(age_og)-np.min(age_og)))*np.max(eigen_values), (eig_vec1[1]*(np.max(salary_og)-np.min(salary_og)))*np.max(eigen_values), color=['r'],units='xy', angles='xy', scale_units='xy', scale=0.2)
            
plt.quiver(np.mean(age_og), np.mean(salary_og), (eig_vec2[0]*(np.max(age_og)-np.min(age_og)))*(eigen_values[1]), (eig_vec2[1]*(np.max(salary_og)-np.min(salary_og)))*(eigen_values[1]), color=['b'],units='xy', angles='xy', scale_units='xy', scale=0.1)

plt.scatter(age_og, salary_og)
plt.xlabel('age')
plt.ylabel('salary')
plt.savefig('results/3_Eigen.png')
plt.show()
