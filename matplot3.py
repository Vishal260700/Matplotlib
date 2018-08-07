import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [4,5,6,7,8]

x2 = [2,4,6,8,10]
y2 = [3,4,5,6,2]

#now we are going to show upon the bar charts so we added the color attribute to distingiush different bars

plt.bar(x,y,label = "bar1" , color = 'red')
plt.bar(x2,y2,label = "bar2" , color = 'blue')

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('interesting bar chart')

plt.legend()

plt.show()