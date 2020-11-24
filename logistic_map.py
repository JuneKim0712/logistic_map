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
 
 
class LogisticMap:
    def __init__(self):
        self.growth_rate = np.float(0)
        self.initial = 0.5
        self.all_result = np.array([], dtype=float)
        self.test_initial = self.initial
        self.limit = 4.0
    
    def plot(self, finding, times):
        times += 100
        while times > 1:
            self.all_result = np.append(self.all_result,
                                        np.array([self.growth_rate * self.test_initial * (1 - self.test_initial)]))
            self.test_initial = self.all_result[-1]
            times -= 1
            continue

        self.test_initial = self.initial

        if finding == 'plots':
            return self.all_result
        else:
            return simplify(self.all_result[100:])
    
    def graph(self, plot_t, per):
        round_up = len(str(per)) - 1
        while self.growth_rate < self.limit:
            self.all_result = np.array([])
            plt.clf()
            plt.plot(self.plot('plots', plot_t), marker='o', markersize=5, markerfacecolor='k')
            plt.plot(0, 0)
            plt.xlabel('Times')
            plt.title('growth rate: ' + str(self.growth_rate))
            plt.ylabel('number of result')
            plt.draw()
            plt.pause(0.00001)
            self.growth_rate = np.round(self.growth_rate + per, round_up)
            continue
        return

    def graph_2(self, plot_t, per):
        round_up = len(str(per)) - 1
        plt.plot(4, 1)
        plt.ylabel('Equilibrium')
        plt.xlabel('growth rate')
        while self.growth_rate < 1:
            plt.plot(self.growth_rate, 0, 'ro', markersize=0.5, markerfacecolor='k', mec='k')
            plt.pause(0.000001)
            self.growth_rate = np.round(self.growth_rate + per, round_up)
        while self.growth_rate < self.limit:
            self.all_result = np.array([], dtype=float)
            y = self.plot('equilibrium', plot_t)
            plt.plot([self.growth_rate] * (len(y)), y, 'ro', markersize=0.5, markerfacecolor='k', mec='k')
            plt.pause(0.000001)
            self.growth_rate = np.round(self.growth_rate + per, round_up)
            continue
        plt.show()
        return

    def graph_2_config(self, plot_t, per):
        round_up = len(str(per)) - 1
        plt.plot(4, 1)
        plt.ylabel('Equilibrium')
        plt.xlabel('growth rate')
        while self.growth_rate < 1:
            plt.plot(self.growth_rate, 0, 'ro', markersize=0.1, markerfacecolor='k', mec='k')
            self.growth_rate = np.round(self.growth_rate + per, round_up)
        while self.growth_rate < self.limit:
            self.all_result = np.array([], dtype=float)
            y = self.plot('equilibrium', plot_t)
            plt.plot([self.growth_rate] * (len(y)), y, 'ro', markersize=0.1, markerfacecolor='k', mec='k')
            self.growth_rate = np.round(self.growth_rate + per, round_up)
            continue
        plt.show()
        return

    def graphall(self, plot_t1, plot_t2, per):
        round_up = len(str(per)) - 1
        right = plt.subplot(212)
        right.plot(self.limit, 1)
        left = plt.subplot(211)
        left.plot(0, 0)

        while self.growth_rate < 1:
            self.all_result = np.array([], dtype=float)
            self.growth_rate = np.round(self.growth_rate + per, round_up)
            left.cla()
            plt.title('growth rate: ' + str(self.growth_rate))
            right.set_title('population vs growth rate')
            left.plot(self.plot('plot', plot_t1), marker='o', markersize=5, markerfacecolor='k')
            right.plot(self.growth_rate, 0, 'ro', markersize=2, markerfacecolor='k', mec='k')
            left.plot(0, 0)
            plt.pause(0.000001)
            continue

        while self.growth_rate < self.limit:
            self.all_result = np.array([], dtype=float)
            self.growth_rate = np.round(self.growth_rate + per, round_up)
            left.cla()
            plt.title('growth rate: ' + str(self.growth_rate))
            y = self.plot('equilibrium', plot_t2)
            right.plot([self.growth_rate] * (len(y)), y, 'ro', markersize=2, markerfacecolor='k', mec='k')
            self.all_result = np.array([], dtype=float)
            left.plot(self.plot('plots', plot_t1), marker='o', markersize=5, markerfacecolor='k')
            left.plot(0, 0)
            plt.pause(0.0000001)
            continue

        return
