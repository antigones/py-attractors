import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lorenz_eq(t,state,P,R,B):
    x,y,z = state

    dx_dt = P*(y-x)
    dy_dt = R*x-y-x*z
    dz_dt = x*y - B*z

    return [dx_dt,dy_dt,dz_dt]

t_interval = (0,30)
start_state = [1,1,1]

P = 10
R = 28
B = 8/3

sol = solve_ivp(lorenz_eq, t_interval, start_state, args=(P,R,B))

img = plt.figure().add_subplot(projection='3d')
img.plot(sol.y[0], sol.y[1], sol.y[2])
plt.show()
