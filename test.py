import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.signal import max_len_seq

fs = 10e6
rs = 10e5
ns = fs // rs
 

data = max_len_seq(8)[0] 
data = np.concatenate((data,np.zeros(1)))
 
 
x_ = np.array([1,1,1,-1,-1,-1,1,-1,-1,1,-1])
b7 = np.array([1,-1,1,1,1,-1,1])
ts1 = np.array([0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1])
ts2 = [0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1]
ts3 = [1,0,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,1]
ts4 = [1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0]
m = 2*data-1
#ts1t=2*ts1-1
ts1t = b7
 

b = np.ones(int(ns))
 
#qpsk

 
x=np.reshape(m,(2,128))
xi=x[0,:]
xq=x[1,:]
x_bb=(xi+1j*xq)/np.sqrt(2)
plt.figure(1)
plt.scatter(x_bb.real,x_bb.imag)
plt.show()


file = open("buffer.h", "w")
file.write("double arr_real[] = {")
index = 0
for elem in x_bb:
    str_elem = f"{elem.real}, "
    file.write(str_elem + "\n")
    index += 1
print(index)
file.write("};")
file.write("\ndouble arr_imag[] = {")
for elem in x_bb:
    str_elem = f"{elem.imag}, "
    file.write(str_elem + "\n")
file.write("};")
file.close()

 
 
# xiq=2**14*x_bb
 
# n_frame= len(xiq)
# xrec1=sdr.rx()
# xrec = xrec1/np.mean(xrec1**2)
# plt.figure(2)
# plt.scatter(xrec.real,xrec.imag)