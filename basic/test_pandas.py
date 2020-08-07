import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame


obj = pd.Series([4,7,5,3])
print(obj)

obj2 = pd.Series([4,7,5,3],index=['a','d','c','b'])
print(obj2)

obj.plot.bar()
plt.savefig('./image/bar.png')

        
