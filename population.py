import numpy as np

from solutions_animation import SolutionAnimation

def logistic_eq(R: float, x_cur: float) -> float:
    x_next = R*x_cur*(1-x_cur)
    return x_next

solutions = list()
labels = list()
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
    labels.append(r)
    solutions.append(xs)
        
SolutionAnimation(solutions,labels).save_animation('anim.gif')