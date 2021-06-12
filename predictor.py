#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow as tf
import numpy as np
import pandas as pd
import sklearn
import joblib


# In[4]:


def predictRuns(testInput):
    with open('venue_encoder.joblib','rb') as v:
        venue_encoder=joblib.load(v)
    with open('team_encoder.joblib','rb') as t:
        team_encoder=joblib.load(t)
    model=tf.keras.models.load_model('my_model.h5')
    
   
    test=pd.read_csv(testInput)
   
    test['venue']=venue_encoder.transform(test['venue'])
    test['batting_team']=team_encoder.transform(test['batting_team'])
    test['bowling_team']=team_encoder.transform(test['bowling_team'])
    
    test=test[['venue','innings','batting_team','bowling_team']]
    test=test.to_numpy()
    
    test=tf.convert_to_tensor(test,dtype='float32')
    test=tf.reshape(test,[-1,4])
    test=tf.keras.utils.normalize(test)
    output=model.predict(test)
    output=np.array(output)
    output=np.rint(output)
    output=output.astype('int')
    output1=output.flatten()
    return output1
    
    
    


# In[ ]:




