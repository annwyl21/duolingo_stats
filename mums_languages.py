import datetime 
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

df_leaderboard = pd.read_csv('duolingo_leaderboards.csv')
print(df_leaderboard.head())

#Dataframe storing information about my language studies
df = pd.DataFrame({
  'Language': ['Dutch', 'Welsh', 'Scots Gaelic', 'German', 'Spanish', 'French', 'Swedish'],
  #'Irish', 'Russian', 'Greek', 'Italian', 'Polish', 'Swahili', 'Mandarin', 'Japanese'
  'Duolingo Checkpoint Passed': [2, 1, 1, 2, 2, 3, 0],
  'Crowns': [203, 102, 81, 175, 288, 226, 4],
  'Words': [1056, 465, 398, 444, 1518, 1867, 25],
  })
#extra line in dataframe to store XP points
df['Duolingo XP'] = [18588, 10730, 11819, 14163, 41757, 22829, 641]
df['Days Active'] = [189, 131, 126, 130, 302, 271, 4]
df['Number of Lessons Completed'] = [1206, 699, 772, 782, 1722, 1355, 21]

sns.set_style("darkgrid")
sns.set_palette("muted")#deep, muted, pastel, bright, dark, and colorblind
sns.set_context('notebook', font_scale=0.7)

ax=plt.subplots()
#Bar Chart Languages Learned and Level Achieved
ax1=plt.figure(figsize=(5,4))
ax1=plt.subplot()
ax1=sns.barplot(data=df, x='Language', y='Duolingo Checkpoint Passed')
ax1=plt.title('Current Level in Languages Learned')
ax1.set_yticks((1, 2, 3))
ax1.set_yticklabels(('Level 1', 'Level 2', 'Level 3'))

# #Pie Chart Crowns Earned in each Language
# ax2=plt.figure(figsize=(4,4))
# ax2=plt.subplot()
# ax2=plt.pie(df['Crowns'], autopct='%d%%')
# ax2=plt.axis('equal')
# ax2=plt.title("Duolingo Crowns Earned in each Language")
# ax2=plt.legend(df['Language'], loc='upper left')

# #Pie Chart XP
# ax3=plt.figure(figsize=(4,4))
# ax3=plt.subplot()
# ax3=plt.pie(df['Duolingo XP'], autopct='%d%%')
# ax3=plt.axis('equal')
# ax3=plt.title('Duolingo XP earned in each Language')
# ax3=plt.legend(df['Language'], loc='upper left')

# #Words learned by level of vocabulary in each language
# ax4=plt.figure(figsize=(6,5))
# ax4=plt.subplot()
# ax4=sns.barplot(data=df, x='Language', y='Words', hue='Duolingo Checkpoint Passed')
# ax4=plt.title('Complexity of Vocabulary')

#Distribution of League Scores
#KDE distribution
#sns.kdeplot(df_leaderboard['score'], shade=True)
# box plots, showing outliers
#sns.boxplot(data=df_leaderboard, x='score')
# violin plot
#sns.violinplot(data=df_leaderboard, x='score')

#Scores in each League
# sns.barplot(data=df_leaderboard, x='tier', y='score')
# plt.title('How does each leaderboard influence my weekly score?')

#Scatterplot to show days active against the number of lessons completed
#sns.scatterplot(x=df['Days Active'], y=df['Number of Lessons Completed'], hue=df['Language'])
#plt.title('How does length of time learning affect the number of lessons I complete?')



plt.show()
