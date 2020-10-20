import matplotlib.pyplot as plt
import time as t
import numpy as np


class graphit:
    def __init__(self, initial_population, growth_rate):
        self.gr_rate = growth_rate
        self.initial = initial_population
        self.all_result = np.array([], dtype=float)
        self.test_popul = initial_population

    def show(self, times):
        while True:
            if times < 1:
                self.test_popul = self.initial
                return self.all_result
            self.all_result = np.append(self.all_result,
                                        np.array([self.gr_rate * self.test_popul * (1 - self.test_popul)]))
            self.test_popul = self.all_result[-1]
            times -= 1
            continue

    def graphcl(self, limit, show_t, grpt):
        grpt = grpt * 10000
        while self.gr_rate > limit:
            self.all_result = np.array([])
            plt.clf()
            plt.plot(self.show(show_t), marker='o', markersize=5, markerfacecolor='k')
            plt.xlabel('Times')
            plt.title('growth rate: ' + str(self.gr_rate))
            plt.ylabel('number of result')
            plt.draw()
            plt.pause(0.00001)
            self.gr_rate = (round(round(round(round(self.gr_rate, 4) * 10, 4) * 10, 4) * 10, 4) * 10 + grpt) / 10000
            continue


g = graphit(0.5, 0)
g.graphcl(4.0, 100, 0.01)

