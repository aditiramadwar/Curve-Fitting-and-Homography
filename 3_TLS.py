import matplotlib.pyplot as plt
import numpy as np
import csv
def eig_sort(val,vec):
	idx = val.argsort()[::-1]   
	val = val[idx]
	vec = vec[:,idx]
	return val,vec

def svd(A):
    length = min(A.shape[0], A.shape[1])
    AAT = np.dot(A, A.transpose())
    eigen_values_aat, eigen_vectors_aat = np.linalg.eig(AAT)
    eigen_values_aat, eigen_vectors_aat = eig_sort(eigen_values_aat,eigen_vectors_aat)
    singular_val = np.sqrt(eigen_values_aat)
    sigma = np.zeros((np.shape(A)))
    np.fill_diagonal(sigma, singular_val)
    ATA = np.dot(A.transpose(), A)
    eigen_values_ata, eigen_vectors_ata = np.linalg.eig(ATA)
    eigen_values_ata, eigen_vectors_ata = eig_sort(eigen_values_ata, eigen_vectors_ata)
    VT = eigen_vectors_ata.transpose()
    u = []
    for i in range(0,len(singular_val)):
        u.append((1/singular_val[i])*np.dot(A, VT[i]))
    return np.array(u).transpose(),sigma,VT

age = []
salary = []
file = open('data/ENPM673_hw1_linear_regression_dataset.csv')
csvreader = csv.reader(file)
header = next(csvreader)
for row in csvreader:
    age = np.append(age, int(row[0]))
    salary = np.append(salary, float(row[6]))
file.close()

x_n = (age - np.min(age)) / (np.max(age) - np.min(age))
y_n = (salary - np.min(salary)) / (np.max(salary) - np.min(salary))
x_mean = np.mean(x_n)
y_mean = np.mean(y_n)
U = np.vstack([x_n - x_mean, y_n - y_mean]).transpose()
A = np.dot(U.transpose(), U)
U, S, VT = svd(A)
V = VT.T
X = V[:, V.shape[1]-1]
a = X[0]
b = X[1]
d = a*x_mean + b*y_mean
m = -a / b
c = d / b
curve_n = m*x_n + c
curve = curve_n * (np.max(salary) - np.min(salary))+np.min(salary)
plt.plot(age, curve, 'r')
plt.scatter(age, salary)
plt.xlabel('age')
plt.ylabel('salary')
plt.savefig('results/3_TLS.png')
plt.show()
