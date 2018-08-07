import matplotlib.pyplot as plt

population = [3,23,21,55,77,110,56,23,56,23,89,2,1,25,78]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

# we are using histograms to classigy data of population in bins category

plt.hist(population , bins , label = "Histogram of population of a community",rwidth = 0.8)

# we used rwidth 0.8 as to reduce overlapping

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('interesting Histogram')

plt.legend()

plt.show()