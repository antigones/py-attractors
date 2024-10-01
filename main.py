import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
from scipy.integrate import solve_ivp

def lorenz_eq(t,state,S,R,B):
    x,y,z = state

    dx_dt = S*(y-x)
    dy_dt = R*x-y-x*z
    dz_dt = x*y-B*z

    return [dx_dt,dy_dt,dz_dt]

def draw(solutions:list,colors:np.ndarray,filename:str):
    img = plt.figure(clear=True).add_subplot(projection='3d')
    for i,solution in enumerate(solutions):
        img.plot(solution.y[0], solution.y[1], solution.y[2],color=colors[i])
    plt.savefig(filename)

def animate(solutions:list,colors:np.ndarray,dir:str):
    graph_bounds = 25
    for t in range(len(solutions[0].y[0])):
        img = plt.figure(clear=True).add_subplot(projection='3d')
        img.set_xlim((-graph_bounds,graph_bounds))
        img.set_ylim((-graph_bounds,graph_bounds))
        img.set_zlim((-graph_bounds,graph_bounds))

        img.set_xticks(list(range(-graph_bounds,graph_bounds,10)))
        img.set_yticks(list(range(-graph_bounds,graph_bounds,10)))
        for i,solution in enumerate(solutions):
            img.plot(solution.y[0][:t], solution.y[1][:t], solution.y[2][:t],color=colors[i])
            
        plt.tight_layout()    
        plt.savefig(f'{dir}/frame{t:05}.png')
        plt.close()
    
    files = os.listdir(dir)
    image_files = sorted([file for file in files if file.endswith(('.png'))])
    
    images = [Image.open(dir+'/'+image) for image in image_files]
    images[0].save(fp=dir+'/animation.gif', format='GIF', append_images=images[1:],save_all=True,loop=0)
    
    

cmap = mpl.colormaps['viridis']
t_interval = (0,30)
start_state = [1,1,1]

S = 10
R = 28
B = 8/3
solutions = list()

N_SOL = 5
delta = 0
for i in range(N_SOL):
    start_state = [1+delta,1+delta,1+delta]
    sol = solve_ivp(lorenz_eq, t_interval, start_state, args=(S,R,B))
    solutions.append(sol)
    delta = delta + 0.001

colors = cmap(np.linspace(0, 1, N_SOL))
# draw(solutions=solutions,colors=colors,filename='lorenz_changing_r.png')
animate(solutions=solutions,colors=colors, dir='./animation')
