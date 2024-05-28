# Issac
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

defending=pd.read_csv(r"C:\Users\i7 11Th\Desktop\Python2Proj\Data\defending.csv")
goalkeeping=pd.read_csv(r"C:\Users\i7 11Th\Desktop\Python2Proj\Data\goalkeeping.csv")
# Code preparation
# Calculating Score of defending of each football club
defending['Score'] = defending['t_won'] / defending['tackles'] * 100 * 0.4 + defending['balls_recoverd'].fillna(0) / \
                    defending['balls_recoverd'].sum() * 100 * 0.3 + \
                    defending['clearance_attempted'].fillna(0) / defending['clearance_attempted'].sum() * 100 * 0.3


# Calculating Score of goalkeeping of each football club
goalkeeping['Scorekeeping'] = (
       goalkeeping['saved'] / (goalkeeping['saved'] + goalkeeping['conceded']) * 100 * 0.4 +
       goalkeeping['saved_penalties'].fillna(0) / goalkeeping['saved_penalties'].sum() * 100 * 0.3 +
       goalkeeping['cleansheets'].fillna(0) / goalkeeping['cleansheets'].sum() * 100 * 0.2 +
       goalkeeping['punches made'].fillna(0) / goalkeeping['punches made'].sum() * 100 * 0.1
)


# Filtering players who didn't play 2 or more games, should I add it ?
# defending_less2 = defending[defending['match_played'] >= 2]
# goalkeeping_less2 = goalkeeping[goalkeeping['match_played'] >= 2]




# Calculating the average Score for each club's player in defending
average_scores_defending = defending.groupby('club')['Score'].mean()
# Calculating the average Score of goalkeeping in different clubs
average_scores_goalkeeping = goalkeeping.groupby('club')['Scorekeeping'].mean()


print(average_scores_defending)
df=(average_scores_defending)
df.to_csv('avg_score_defending.csv', index=True)
print("===============")
print(average_scores_goalkeeping)
df=(average_scores_goalkeeping)
df.to_csv('avg_score_goalkeeping.csv', index=True)


# Colour of the bar, I am using the iconic colour of each team
Colour = ["#0097DB", '#F9CC11', '#65B32E', '#E70005', '#008057', '#FDCC00', '#F0612C', '#F43333', '#DF003C', '#FEBE10', '#00428C', '#004170', '#FB090B', '#DA291C', '#6CABDD', '#008ECB', '#C8102E', '#DD0741', '#E01E13', '#000000', '#010E80', '#176FC1', '#FDE100', '#0078BF', '#034694', '#000000','#E83030', '#0066B2', '#004D98', '#272E61', '#1E71B8', '#D2122E']
reversed_colour = Colour[::-1]


# Making a horizontal bar chart
average_scores_defending.plot(kind='barh', color=reversed_colour)
# Giving a label to show what is x-axis and y-axis is representing
plt.xlabel('Football Club')
plt.ylabel('Average Score')
# Giving a title for the graph
plt.title('defending score in average in different football club')
# Since there is too many club in the database so the graph will be too tight
# with this code can make the graph more readable
plt.tight_layout()
# Giving grid to the graph so that it is easier to compare bar that having similar score
plt.grid()
plt.show()


# Making a bar chart
average_scores_goalkeeping.plot(kind='bar', color='red')
# Giving a label to show what is x-axis and y-axis is representing
plt.xlabel('Football Club')
plt.ylabel('Average Score of their goalkeeping')
# Giving a title for the graph
plt.title('Average goalkeeping score of each football club')
# Because the FC's name is too long, so it will present it vertically, but it is not readable
# rotate it to make it to be more readable
plt.xticks(rotation=50, ha='right')
# Since there is too many club in the database so the graph will be too tight
# with this code can make the graph more readable
plt.tight_layout()
# Giving grid to the graph so that it is easier to compare bar that having similar score
plt.grid()
plt.show()

