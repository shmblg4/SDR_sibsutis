import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.signal import max_len_seq
import json



# sdr.rx_lo = 2000000000
# sdr.tx_lo = 2000000000
# sdr.tx_cyclic_buffer = True
# #sdr.tx_cyclic_buffer = False
# sdr.tx_hardwaregain_chan0 = -5
# sdr.gain_control_mode_chan0 = "slow_attack"


fs = 1000000
rs = 100000
ns = fs // rs
 

data = max_len_seq(8)[0] 
data = np.concatenate((data,np.zeros(1)))
 
 
x_ = np.array([1,1,1,-1,-1,-1,1,-1,-1,1,-1])
m=2*data-1
 

b = np.ones(int(ns))
 
#qpsk

 
x=np.reshape(m,(2,128))
xi=x[0,:]
xq=x[1,:]
x_bb=((xi+1j*xq)/np.sqrt(2) * 2**8)

x_cc = np.repeat(x_bb, 10)

plt.figure(1)
plt.scatter(x_cc.real,x_cc.imag)
 
plt.show()





with open('buffer.h', 'w') as file:
    file.write("#ifndef MYFILE_H\n")
    file.write("#define MYFILE_H\n\n")
    
    file.write("const double x_bb_real[] = {")
    file.write(', '.join(map(str, x_cc.real)))
    file.write("};\n")
    
    file.write("const double x_bb_imag[] = {")
    file.write(', '.join(map(str, x_cc.imag)))
    file.write("};\n\n")
    
    file.write("#endif // MYFILE_H\n")



# xiq=2**14*x_bb
 
# n_frame= len(xiq)
# sdr.tx(xiq)

# sdr.rx_rf_bandwidth = 1000000
# sdr.rx_destroy_buffer()
# sdr.rx_hardwaregain_chan0 = -5
# sdr.rx_buffer_size =2*n_frame
# xrec1=sdr.rx()
# xrec = xrec1/np.mean(xrec1**2)
# plt.figure(2)
# plt.scatter(xrec.real,xrec.imag)