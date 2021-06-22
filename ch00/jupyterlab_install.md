# Jupyter Lab Installation

- Install python at [python.org](https://python.org)
- Install following python modules from the terminal
    - `pip install sympy`
    - `pip install numpy`
    - `pip install matplotlib`
    - `pip install jupyterlab`
    - `pip install qtconsole`
    - `pip install ipywidgets`
    - `pip install ipympl`
- Check `jupyter-lab` from the terminal
    - `jupyter-lab`

# Test interactive matplotlib 


```
%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
l1=ax.plot(x1,y,'ys-')
l2=ax.plot(x2,y,'go--') 
ax.legend(labels=('tv', 'Smartphone'), loc='upper left')
plt.savefig("sales.png")
```
