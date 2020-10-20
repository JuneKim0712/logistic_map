import matplotlib.pyplot as plt
import time as t
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
        while 0 == 0:
            if times < 1:
                self.test_popul = self.initial
                return simplify(self.all_result[175:])
            self.all_result = np.append(self.all_result,
                                        np.array([self.gr_rate * self.test_popul * (1 - self.test_popul)]))
            self.test_popul = self.all_result[-1]
            times -= 1
            continue

    def graphcl(self, limit, show_t, grpt):
        round_up = len(str(grpt))
        plt.plot(4, 1)
        while 0 == 0:
            if self.gr_rate > limit:
                plt.show()
                return
            self.all_result = np.array([], dtype=float)
            y = self.show(show_t)
            plt.plot([self.gr_rate] * (len(y)), y, 'ro', markersize=1, markerfacecolor='k', mec='k')
            plt.xlabel('growth rate')
            plt.ylabel('result')
            self.gr_rate = np.round(self.gr_rate + grpt, round_up)
            continue


tm = t.time()
g = graphit(0.5, 0)
g.graphcl(4, 600, 0.0001)
print(t.time()-tm)





# """ note: June, Please make it another version to show the result but not the progress """



 