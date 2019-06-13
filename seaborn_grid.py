import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""There are five preset seaborn themes:darkgrid,whitegrid,dark,white and ticks.
The default theme is darkgrid"""

sns.set_style("dark")
data=np.random.normal(size=(20,9)) + np.arange(9)/2
sns.boxplot(data=data)
sns.spines
plt.show()
