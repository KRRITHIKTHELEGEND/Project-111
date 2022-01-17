import plotly.figure_factory as ff 
import pandas as pd
import plotly.graph_objects as go 
import statistics
import csv
import random
import os

os.system('cls')

df = pd.read_csv('medium_data.csv')
data = df['claps'].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("\n Mean                           :   ", mean)
print(" Standard Deviation             :   ", std_deviation)

fig = ff.create_distplot([data], ["claps"], show_hist = False)

def random_set_of_mean(counter):

    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print(" Mean Of Sampling Distribution  :   ", mean)
fig1 = ff.create_distplot([mean_list], ["responses"], show_hist = False)
fig1.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation 
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation) 
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation) 
print(" Standard Deviation 1           :   ",first_std_deviation_start, first_std_deviation_end) 
print(" Standard Deviation 2           :   ",second_std_deviation_start, second_std_deviation_end)
print(" Standard Deviation 3           :   ",third_std_deviation_start,third_std_deviation_end)

fig2 = ff.create_distplot([mean_list], ["responses"], show_hist=False) 
fig2.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig2.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START")) 
fig2.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig2.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START")) 
fig2.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig2.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START")) 
fig2.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

mean_of_sample1 = statistics.mean(data) 
print(" Mean Of Sample 1               :   ",mean_of_sample1) 
fig3 = ff.create_distplot([mean_list], ["reponses"], show_hist=False) 
fig3.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig3.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE")) 
fig3.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))

z_score = (mean_of_sample1 - mean) / std_deviation
print(" The Z Score                    :   ", z_score)

fig.show()
fig1.show()
fig2.show()
fig3.show()