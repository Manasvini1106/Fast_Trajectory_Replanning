import matplotlib.pyplot as plt

forwardadistance = [202, 202, 200, 200, 200, 200, 200, 208, 200, 200, 206, 200, 200, 202, 204, 202, 202, 200, 200, 202,
                    202]
forwardatime = [52.9126, 32.8616, 24.9036, 33.3679, 31.4062, 19.3306, 36.1430, 31.7340, 46.8530, 14.6291, 17.3908,
                40.4951, 23.1076, 19.8260, 45.5777, 26.1447, 19.8403, 20.7861, 35.8485, 16.6155, 43.1553]
backwardadistance = [202, 202, 200, 200, 200, 200, 200, 208, 200, 200, 206, 200, 200, 202, 204, 202, 202, 200, 200, 202,
                     202]
backwardatime = [12.9504, 42.9122, 4.9804, 7.2151, 11.9886, 14.1668, 23.9011, 89.1119, 13.4337, 7.9302, 72.2380, 7.1148,
                 5.7932, 7.1990, 35.0213, 34.2082, 34.3689, 9.2645, 6.0131, 41.1020, 7.6425]
adaptiveadistance = [202, 202, 200, 200, 200, 200, 200, 208, 200, 200, 206, 200, 200, 202, 204, 202, 202, 200, 200, 202,
                     202]
adaptiveatime = [38.2162, 26.1631, 23.1180, 22.9189, 31.5173, 32.3041, 31.2667, 38.9505, 13.6713, 13.4689, 9.1459,
                 40.5199, 6.9612, 18.0351, 12.3527, 7.4396, 9.4881, 10.9519, 18.3945, 6.4907, 28.8441]


'''Plotting the algorithms with respect to their run time for different h(manhattan) distances'''
fig, axs = plt.subplots(3)
fig.suptitle('Repeated Forward A* vs Repeated Backward A* vs Adaptive A*')
axs[0].scatter(forwardatime, forwardadistance, color='red')
axs[0].set_title('Repeated Forward A*')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Repeated Forward A*')
axs[1].scatter(backwardatime, backwardadistance, color='green')
axs[1].set_title('Repeated Backward A*')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Repeated Backward A*')
axs[2].scatter(adaptiveatime, adaptiveadistance)
axs[2].set_title('Adaptive A*')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Adaptive A*')
fig.tight_layout()
fig.savefig('comaprison.png')
plt.show()
