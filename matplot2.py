import matplotlib.pyplot as plt

# in reality we will have x,y,x2,y2 as functions

x = [2,3,5]
y = [7,4,9]
x2= [1,2,3]
y2= [13,6,8]

# we are giving labels to lines

plt.plot(x,y,label = "First Line")
plt.plot(x2,y2,label = "Second line")

#labels to axis

plt.xlabel('xlabel')
plt.ylabel('ylabel')

#title of graph with a subheading after \n too

plt.title('Interesting graph depecting\n Legends||labels')

# show us the legend aka the line color for each seperate graph

plt.legend()

#finally showing the graph

plt.show()