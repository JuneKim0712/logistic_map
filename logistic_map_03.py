import matplotlib.pyplot as plt
import time as t
import timeit
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
        self.gr_rate = np.float(growth_rate)
        self.initial = initial_population
        self.all_result = np.array([], dtype=float)
        self.test_popul = initial_population
 
    def show2(self, times):
        while times > 1:
            self.all_result = np.append(self.all_result,
                                        np.array([self.gr_rate * self.test_popul * (1 - self.test_popul)]))
            self.test_popul = self.all_result[-1]
            times -= 1
            continue
        self.test_popul = self.initial
        return simplify(self.all_result[200:])

    def show1(self, times):
        while times > 1:
            self.all_result = np.append(self.all_result,
                                        np.array([self.gr_rate * self.test_popul * (1 - self.test_popul)]))
            self.test_popul = self.all_result[-1]
            times -= 1
            continue

        self.test_popul = self.initial
        return self.all_result

    def graphall(self, limit, show_t1, show_t2, grpt):
        round_up = len(str(grpt)) - 1
        right = plt.subplot(212)
        right.plot(limit, 1)
        left = plt.subplot(211)
        left.plot(0, 0)
        
        while self.gr_rate < 1:
            self.all_result = np.array([], dtype=float)
            self.gr_rate = np.round(self.gr_rate + grpt, round_up)
            left.cla()
            plt.title('growth rate: ' + str(self.gr_rate))
            right.set_title('population vs growth rate')
            left.plot(self.show1(show_t1), marker='o', markersize=5, markerfacecolor='k')
            right.plot(self.gr_rate, 0, 'ro', markersize=2, markerfacecolor='k', mec='k')
            left.plot(0, 0)
            plt.pause(0.000001)
            continue

        while self.gr_rate < limit:
            self.all_result = np.array([], dtype=float)
            self.gr_rate = np.round(self.gr_rate + grpt, round_up)
            left.cla()
            plt.title('growth rate: ' + str(self.gr_rate))
            y = self.show2(show_t2)
            right.plot([self.gr_rate] * (len(y)), y, 'ro', markersize=2, markerfacecolor='k', mec='k')
            self.all_result = np.array([], dtype=float)
            left.plot(self.show1(show_t1), marker='o', markersize=5, markerfacecolor='k')
            left.plot(0, 0)
            plt.pause(0.0000001)
            continue
        return
 
 
tm = t.time()
g = graphit(0.5, 0)
g.graphall(4, 50, 600, 0.01)
print(t.time() - tm)
