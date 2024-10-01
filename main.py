import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def lorenz_eq(t,state,S,R,B):
    x,y,z = state

    dx_dt = S*(y-x)
    dy_dt = R*x-y-x*z
    dz_dt = x*y-B*z

    return [dx_dt,dy_dt,dz_dt]

def draw(solutions:list,colors:np.ndarray):
    img = plt.figure().add_subplot(projection='3d')
    for i,solution in enumerate(solutions):
        img.plot(solution.y[0], solution.y[1], solution.y[2],color=colors[i])
    plt.show()

def animate(solutions:list,colors:np.ndarray):
    pass

cmap = mpl.colormaps['plasma']
t_interval = (0,30)
start_state = [1,1,1]

S = 10
R = 28
B = 8/3
solutions = list()

N_SOL = 5
for i in range(N_SOL):
    sol = solve_ivp(lorenz_eq, t_interval, start_state, args=(S,R,B))
    solutions.append(sol)
    R = R + 0.0001

colors = cmap(np.linspace(0, 1, N_SOL))
draw(solutions=solutions,colors=colors)


