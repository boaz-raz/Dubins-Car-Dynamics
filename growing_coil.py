import dubins
import math
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 
plt.style.use('dark_background')

fig = plt.figure()

q0 = (0.0, 0.0, math.pi/4)
q1 = (-4.0, 4.0, -math.pi)
turning_radius = 1.0
step_size = 0.5

ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50)) 
line, = ax.plot([], [], lw=2)


# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points 
xdata, ydata = [], [] 



# animation function 
def animate(i):
	# path = dubins.shortest_path(q0, q1, turning_radius)
	# configurations, _ = path.sample_many(step_size)
	# print(configurations)
	print("************")
	# for x in configurations:
	# 	print(x)
    # return configurations
	# t is a parameter
	t = 0.1*i
	
	# x, y values to be plotted 
	x = t*np.sin(t)
	y = t*np.cos(t)
	print(x)
	# appending new points to x, y axes points list 
	xdata.append(x)
	ydata.append(y)
	line.set_data(xdata, ydata) 
	return line, 

	
# setting a title for the plot 
plt.title('Creating a growing coil with matplotlib!') 
# hiding the axis details 
plt.axis('off') 

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=500, interval=20, blit=True) 

# save the animation as mp4 video file 
anim.save('coil.gif',writer='imagemagick') 
