import matplotlib.pyplot as plt
import numpy as np

# we can also use csv file reader but numpy is much easier

x , y = np.loadtxt('example.txt',delimiter = ',' ,unpack = True) # delimiter means what differentiates the parts of txt file
plt.plot(x,y,label = "file readed plot")

plt.title('interesting Scatter plot')
plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.legend()

plt.show()