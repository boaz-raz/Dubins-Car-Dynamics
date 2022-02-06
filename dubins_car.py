import dubins
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure(figsize=(10,10))
q0 = (2.0, 1.0, math.pi/10)
#q0 = (0.0, 0.0, math.pi/4)
q1 = (-4.0, 4.0, -math.pi/10)
# q0 = (0.0, 0.0, math.pi/4)
# q1 = (-4.0, 4.0, -math.pi)

turning_radius = 1.0
step_size = 0.5

path = dubins.shortest_path(q0, q1, turning_radius)
qs, _ = path.sample_many(step_size)

xsdata, ysdata = [], []
xsdata2, ysdata2 = [], []
xdata, ydata = [],[]

ln,  = plt.plot([], [], 'b-')
ln2, = plt.plot([], [], 'r.')
ln3, = plt.plot([], [], 'r-')

# initialization function 
def init():
    ln.set_data([], [])
    ln2.set_data([], [])
    ln3.set_data([], [])
    
    return ln,ln2,ln3,

# animation function 
def animate(i):
    path = dubins.shortest_path(q0, q1, turning_radius)
    qs, _ = path.sample_many(step_size)
    qs = np.array(qs)
    xs = qs[:, 0]
    ys = qs[:, 1]
    theta = qs[:, 2]
    us = xs + np.cos(qs[:, 2])
    vs = ys + np.sin(qs[:, 2])
    plt.plot(xs, ys, 'b-')
    #plt.plot(xs, ys, 'r.')
    #print(qs)
    xsdata.append(xs[i])
    print("x =", xs[i], "y =", ys[i], "theta =", theta[i])
    ysdata.append(ys[i])
    xsdata2.append(xs)
    ysdata2.append(ys)
    
    # xdata.append([xs[i], us[i]])
    # ydata.append([ys[i], vs[i]])
    ln.set_data(xsdata, ysdata)
    ln2.set_data(xsdata2, ysdata2)
    ln3.set_data(xdata,ydata)
    return ln,ln2,ln3,

# setting a title for the plot 
plt.title('Dubins path!')

# call the animator	 
ani = FuncAnimation(fig, animate, frames=len(qs), interval=500,
                   init_func=init, blit=True, repeat=False)


plt.show()

