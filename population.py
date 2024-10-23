from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt

def logistic_eq(R: float, x_cur: float) -> float:
    x_next = R*x_cur*(1-x_cur)
    return x_next

solutions = list()
t_range = (0,63)
r_range = (2,4)
initial_pop = 0.5
R=3

for r in np.arange(r_range[0], r_range[1], 0.1):
    xs = list()
    cur_pop = initial_pop
    for t in range(*t_range):
        pop_next = logistic_eq(R=r,x_cur=cur_pop)
        xs.append(pop_next)
        cur_pop = pop_next
    solutions.append((r,xs))
        
def update(frame):
    ax.clear()
    r, sol = solutions[frame]
    p = ax.plot(sol,label=f'R = {r:.1f}')
    ax.legend()
   
    return p

plt.figure(clear=True).add_subplot()
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig=fig, func=update, frames=len(solutions), interval=1000)
plt.show()