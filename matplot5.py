import matplotlib.pyplot as plt

x = [1,4,6,2,7,9]
y = [7,4,9,2,8,2]

# scatter plot attributes are different we can google search for each also

plt.scatter(x ,y , label = "scatter plot" , color = "red" , s = 100 , marker = "*")

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('interesting Scatter plot')

plt.legend()

plt.show()