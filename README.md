# logistic_map

Code that Graphs Logistic map in different types and using different values such as times of plotting or showing equilibrium or not

## Features
 - LogisticMap
   - plot
   - graph
   - graph_2
   - graph_2_config
   - graph_all


## LogisticMap
   LogisticMap is a class that contains a plot, graph, graph_2, graph_2_config and graph_all
   
### plot
This function receives finding and times, which finding means are you using this function for equilibrium or not, and times refer to how many iterations are you going to do (caution: this doesn't show a graph, but it gives of raw data)

### graph
This function shows a graph of literation of logistic map equation in live, meaning Growth rate increase every loop

### graph_2
This function shows Growth_rate vs. population in live, which means Growth rate increase every loop

### graph_2_config
graph_2_config is a function that doesn't show in live, rather shows all graph of Graph_2 in one time, making the performance time more faster

### graph_all
This function is a sort of a combination of graph and graph_2, showing in side by side simultaneously

### Arguments
__plot_t__ refers how many plots are going to show in the graph (in graph_all show_t1 refers to graph show_t and show_t2 refers to graph_2 show_t)

__per__ refers how much value of Growth rate is going to increase for every loop

### init (TMI)
you can change the value what ever you want, but this setting is most optimal and the maximum self.limit is 4.0 because if it goes over it becomes 0 or -infinite
``` python
self.growth_rate = np.float(0)
self.initial = 0.5
self.all_result = np.array([], dtype=float)
self.test_initial = self.initial
self.limit = 4.0
```

### example of how to use it
```python
name_of_variable_you_want = LogisticMap
name_of_variable_you_want.graph(100, 0.001)
```
