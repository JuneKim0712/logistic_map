import matplotlib.pyplot as plt
import numpy as np


def simplify(list_):
    list_.sort()
    b = np.array([])
    while True:
        b = np.append(b, list_[0])
        list_ = list_[np.where(list_ > list_[0])]
        if list_.size == 0:
            return b


class graphit:
    def __init__(self, initial_population, growth_rate):
        self.gr_rate = growth_rate
        self.initial = initial_population
        self.all_result = np.array([], dtype=float)
        self.test_popul = initial_population

    def show(self, times):
        while times > 1:
            self.all_result = np.append(self.all_result,
                                        np.array([self.gr_rate * self.test_popul * (1 - self.test_popul)]))
            self.test_popul = self.all_result[-1]
            times -= 1
            continue
        self.test_popul = self.initial
        return simplify(self.all_result[200:])

    def graphcl(self, limit, show_t, grpt):
        round_up = len(str(grpt)) - 1
        plt.plot(4, 1)
        plt.ylabel('Equilibrium')
        plt.xlabel('growth rate')
        while self.gr_rate < 1:
            plt.plot(self.gr_rate, 0, 'ro', markersize=0.5, markerfacecolor='k', mec='k')
            plt.pause(0.000001)
            self.gr_rate = np.round(self.gr_rate + grpt, round_up)
        while self.gr_rate < limit:
            self.all_result = np.array([], dtype=float)
            y = self.show(show_t)
            plt.plot([self.gr_rate] * (len(y)), y, 'ro', markersize=0.5, markerfacecolor='k', mec='k')
            plt.pause(0.000001)
            self.gr_rate = np.round(self.gr_rate + grpt, round_up)
            continue
        plt.show()
        return


g = graphit(0.5, 0)
g.graphcl(4, 300, 0.01)
