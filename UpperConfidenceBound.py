import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Ads_CTR_Optimisation.csv')
N=10000   #no. of Rounds
d=10      #no. of advertisements
add_selected=[]
#implementing UCB
import math as m
numbers_of_selection=[0]*d
sums_of_rewards=[0]*d
total_reward=0
for n in range(0,N):
    ad=0
    max_upper_bound=0
    for i in range(0,d):
        if numbers_of_selection[i]>0:
            average_reward=sums_of_rewards[i]/numbers_of_selection[i]
            delta_i=m.sqrt(3/2* m.log(n+1)/numbers_of_selection[i])
            upper_bound=average_reward+delta_i
        else:
            upper_bound=1e400

        if upper_bound>max_upper_bound:
            max_upper_bound=upper_bound
            ad=i
    add_selected.append(ad)
    numbers_of_selection[ad]+=1
    reward=dataset.values[n,ad]
    sums_of_rewards[ad]=sums_of_rewards[ad]+reward
    total_reward+=reward

print(total_reward)
#print(add_selected)

#visual Representation
plt.hist(add_selected)
plt.title('Histogram of Ad Selection')
plt.xlabel('Ads')
plt.ylabel('Frequency of Selection')
plt.show()



