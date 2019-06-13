

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def sinplot(flip=1):
  """Defining a simple function to plot some offset sine waves,which will help us to see the different stylistic parameters"""
  x=np.linspace(0,14,100) ##linspace is like arange 
  for i in range(1,7):
    plt.plot(x,np.sin(x+ i* .5) * (7-i) * flip)

###To switch the seaborn default,simply call the set() function 
sns.set()
fig=plt.figure()
sinplot(1)
plt.show()
