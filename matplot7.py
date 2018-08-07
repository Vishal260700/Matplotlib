import matplotlib.pyplot as plt

#different type of data set for a particular person and particular day

slices = [3,5,2,6,8]
names = ['sleeping' , 'eating' , 'playing' , 'working' , 'other']
cols = ['c' , 'm' , 'r' , 'k' , 'green']

#the various attribiutes are shown self explaotry of their tasks

plt.pie(slices,labels = names,colors = cols,shadow = True , explode = (0,0,0.2,0,0.1),startangle = 90,autopct = '%1.1f%%')

#autopct show label over the pie part and explode open up the parts from main one

plt.title('interesting Scatter plot')

plt.legend()

plt.show()