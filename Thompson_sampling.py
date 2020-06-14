import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Ads_CTR_Optimisation.csv')
N=10000   #no. of Rounds
d=10      #no. of advertisements
add_selected=[]
#implementing Thompson sample algorithm
import random
number_of_rewards_1=[0]*d
number_of_rewards_0=[0]*d
total_reward=0
for n in range(0,N):
    ad=0
    max_random_draw=0
    for i in range(0,d):
        random_beta=random.betavariate(number_of_rewards_1[i]+1,number_of_rewards_0[i]+1)
        if random_beta>max_random_draw:
            max_random_draw=random_beta
            ad=i
    add_selected.append(ad)
    number_of_rewards_0
    reward=dataset.values[n,ad]
    if reward==1:
        number_of_rewards_1[ad] += 1
    else:
        number_of_rewards_0[ad]+=1
    total_reward+=reward

print(total_reward)
#print(add_selected)

#visual Representation
plt.hist(add_selected)
plt.title('Histogram of Ad Selection')
plt.xlabel('Ads')
plt.ylabel('Frequency of Selection')
plt.show()