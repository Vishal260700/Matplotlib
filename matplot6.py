import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [6,7,11,8,4]
eating = [2,5,2,1,3]
playing = [4,6,4,3,7]
working = [5,4,6,3,5]

# we have a different data set for a particular person for different days of his life

plt.stackplot(days,sleeping,eating,playing,working)


plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('interesting Scatter plot')

plt.legend()

plt.show()