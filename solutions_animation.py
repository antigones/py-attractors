import matplotlib.pyplot as plt
from matplotlib import animation

class SolutionAnimation:

    def __init__(self, solutions, labels, interval=2000):
        self.solutions = solutions
        self.labels = labels
        self.interval = interval
        plt.figure(clear=True).add_subplot()
        self.fig, self.ax = plt.subplots()

    def update(self, frame):
        self.ax.clear()
        solution = self.solutions[frame]
        label = self.labels[frame]
        p = self.ax.plot(solution,label=f'R = {label:.1f}')
        self.ax.legend()
        return p

    def animate(self):
        anim = animation.FuncAnimation(fig=self.fig, func=self.update, frames=len(self.solutions), interval=self.interval)
        plt.show()

    def save_animation(self, filename):
        anim = animation.FuncAnimation(fig=self.fig, func=self.update, frames=len(self.solutions), interval=self.interval)
        anim.save(filename)