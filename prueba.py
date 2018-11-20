#import tds.utils.py
import sys
import matplotlib.pyplot as plt
sys.path.append('../') #allows to import a module in a diff folder\n",
from tds_utils import *
import scipy.signal as sig

N= int(0.020*fs) #length in samples\n",

r = sig.boxcar(N)    #rectangular window\n",
h = sig.hamming(N)      #hamming window\n",
"#La señal es de la misma longitud\n",
t = np.arange(0,len(r))/fs #time in sec\n",
plt.figure(figsize = (7,5))
plt.subplot(211)
plt.plot(t,r)
"#plot rectangular window\n",
plt.xlabel('Time [sec]')
plt.title('Ventana Rectangular')
plt.subplot(212)
plt.plot(t,h)

#plot hamming window\n",
plt.xlabel('Time [sec]')
plt.title('Ventana Hamming')
