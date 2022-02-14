import numpy as np
import cv2
def eig_sort(val,vec):

	idx = val.argsort()[::-1]   
	val = val[idx]
	vec = vec[:,idx]
	return val,vec

def svd(A):
	length = min(A.shape[0], A.shape[1])
	AAT = np.dot(A, A.transpose())
	eigen_values_aat, eigen_vectors_aat = np.linalg.eig(AAT)
	eigen_values_aat,eigen_vectors_aat = eig_sort(eigen_values_aat,eigen_vectors_aat)
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

xs = np.array([5,150,150,5])
ys = np.array([5,5,150,150])
xp = np.array([100,200,220,100])
yp = np.array([100,80,80,200])
A=np.array([[-xs[0],-ys[0],-1,0,0,0,xs[0]*xp[0],ys[0]*xp[0],xp[0]],
			[0,0,0, -xs[0],-ys[0],-1,xs[0]*yp[0],ys[0]*yp[0],yp[0]],

			[-xs[1],-ys[1],-1,0,0,0,xs[1]*xp[1],ys[1]*xp[1],xp[1]],
			[0,0,0, -xs[1],-ys[1],-1,xs[1]*yp[1],ys[1]*yp[1],yp[1]],

			[-xs[2],-ys[2],-1,0,0,0,xs[2]*xp[2],ys[2]*xp[2],xp[2]],
			[0,0,0, -xs[2],-ys[2],-1,xs[2]*yp[2],ys[2]*yp[2],yp[2]],

			[-xs[3],-ys[3],-1,0,0,0,xs[3]*xp[3],ys[3]*xp[3],xp[3]],
			[0,0,0, -xs[3],-ys[3],-1,xs[3]*yp[3],ys[3]*yp[3],yp[3]]])

u,sigma,VT = svd(A)
verify_A = u.dot(sigma.dot(VT))
print("Verification of SVD: ", np.allclose(A, verify_A))

## Homography matrix
L = VT[-1,:] / VT[-1,-1]
H = L.reshape(3, 3)
print("The homography Matrix is: ")
print(H)
