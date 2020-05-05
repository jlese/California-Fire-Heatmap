#!/usr/bin/env python
# coding: utf-8

# In[59]:


get_ipython().system('pip install folium')


# In[74]:


import pandas as pd
import numpy as np
import folium
from folium import plugins
from folium.plugins import HeatMap


# In[75]:


data = pd.read_csv("California_Fire_Incidents.csv")
data.head()


# In[163]:


map_subset = data[['Name','Latitude', 'Longitude', 'AcresBurned', 'Started']].copy()
map_subset.head()


# In[161]:


map_cali = folium.Map(width = 1000, height = 1500, location = [37.481310, -120.194082],tiles = "Stamen Terrain", zoom_start = 6)
map_cali


# In[162]:


map_subset['Latitude'] = map_subset['Latitude'].astype(float)
map_subset['Longitude'] = map_subset['Longitude'].astype(float)

map_heat = [[row['Latitude'],row['Longitude']] for index, row in map_subset.iterrows()]
HeatMap(map_heat, min_opacity = .4, blur = 7).add_to(map_cali)
map_cali


# In[164]:


largest = map_subset[map_subset['AcresBurned'] > 200000]
largest_subset = largest[['Latitude', 'Longitude']]
largest


# In[155]:


map_cali2 = folium.Map(location = [37.481310, -120.194082],tiles = "Stamen Terrain", zoom_start = 6)


# In[156]:


for point in range(0, len(largest)):
    folium.Marker([largest.iloc[point]['Latitude'], largest.iloc[point]['Longitude']],
                        popup=largest.iloc[point]['Name']).add_to(map_cali)


# In[157]:


map_cali


# In[ ]:





# In[ ]:




