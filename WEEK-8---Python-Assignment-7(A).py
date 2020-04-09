#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df1 = pd.DataFrame(data = list(GradeList),columns=['Names', 'Grades'])
df1.head()

import matplotlib.pyplot as plt
plt.plot('Names','Grades',data=df1)
y= df1['Grades'][df1['Names']=='Bob']
plt.annotate('Wow!',xy=('Bob',y.values),xytext=(y.index.values+0.4,y.values),arrowprops=dict(facecolor='black',shrink=0.05))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




