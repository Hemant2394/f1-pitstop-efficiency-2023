import matplotlib.pyplot as plt
import pandas as pd
pit=pd.read_csv('pit_stops.csv')
result=pd.read_csv('results.csv')
constructor=pd.read_csv('constructors.csv')
race=pd.read_csv("races.csv")
race=race.drop(columns=['url','name'])
constructor=constructor.drop(columns=['url'])

ma=pit.merge(result,on=["raceId","driverId"])
mb=ma.merge(race,on=["raceId"])
merge=mb.merge(constructor,on=["constructorId"])

merge["duration_num"]=pd.to_numeric(merge["duration"],errors="coerce")
merge=merge[merge["duration_num"]<=40.0]
merge=merge[merge["year"]==2023]

data=[
    merge[merge["name"]=="Red Bull"]["duration_num"],
    merge[merge["name"]=="McLaren"]["duration_num"],
    merge[merge["name"]=="Ferrari"]["duration_num"],
    merge[merge["name"]=="AlphaTauri"]["duration_num"],
    merge[merge["name"]=="Williams"]["duration_num"],
    merge[merge["name"]=="Aston Martin"]["duration_num"],
    merge[merge["name"]=="Mercedes"]["duration_num"],
]
label=["Red Bull","McLaren","Ferrari","AlphaTauri","Williams","Aston Martin","Mercedes"]
color=["#4781D7","#F47600","#ED1131","#00A1E8","#1868DB","#229971","#00D7B6"]
plt.figure(figsize=(10,6))
graph=plt.boxplot(data,labels=label,patch_artist=True)
for patch,col in zip(graph['boxes'],color):
    patch.set_facecolor(col)
for median in graph['medians']:
    median.set(color='black',linewidth=2)
for flier,col in zip(graph['fliers'],color):
    flier.set(markerfacecolor='none', markeredgecolor=col, alpha=1)
plt.ylabel("Total Pit Lane Duration (Seconds)")
plt.xlabel("Formula 1 Constructor Crew")
plt.title("F1 Pit Stop Operational Efficiency Dashboard | Variance & Consistency Analysis")
ax=plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.grid(True,linestyle='--',alpha=0.7)
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()
