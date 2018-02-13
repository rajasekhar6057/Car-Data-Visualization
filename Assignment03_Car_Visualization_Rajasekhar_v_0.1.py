
# coding: utf-8

# In[9]:

import pandas as pd
import matplotlib.pyplot as plt


# In[15]:

cardata = pd.read_excel('C:\\Users\\rajas\\Desktop\\assignment03-carvisualization-rajasekhar6057-master\\cardata.xls')
cardataNew = cardata[['Engine Size (l)','Cyl','HP','City MPG','Hwy MPG']]

cardataNew[["City MPG", "Hwy MPG"]].mean(axis=1)

plt.plot(cardataNew['HP'])
plt.show()

 


# In[5]:



