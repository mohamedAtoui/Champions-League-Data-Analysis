import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the attacking dataset
attacking = pd.read_csv(r"C:\Users\i7 11Th\Desktop\Python2Proj\Data\attacking.csv")

# Display basic and detailed statistics
print("Basic Statistics for Attacking Data:")
print(attacking.describe())
print("\nDetailed Statistics:")
print(attacking.agg({'assists': ['min', 'max', 'mean', 'std'],
                     'dribbles': ['min', 'max', 'mean', 'std'],
                     'corner_taken': ['sum']}))

# Checking for missing values
print("\nMissing Values:")
print(attacking.isnull().sum())

# Histograms of all numeric features
attacking.hist(figsize=(12, 10))
plt.suptitle('Histograms of All Numeric Features')
plt.show()

# Boxplots for understanding distributions and identifying outliers
plt.figure(figsize=(10, 6))
attacking[['assists', 'dribbles', 'corner_taken']].boxplot()
plt.title('Boxplot of Assists, Dribbles, and Corner Taken')
plt.show()

# Scatter plot of Assists vs Matches Played with a regression line
plt.figure(figsize=(10, 6))
plt.scatter(attacking['assists'], attacking['match_played'], color='blue')
plt.plot(np.unique(attacking['assists']), np.poly1d(np.polyfit(attacking['assists'], attacking['match_played'], 1))(np.unique(attacking['assists'])), color='red')
plt.title('Assists vs Matches Played with Regression Line')
plt.xlabel('Assists')
plt.ylabel('Matches Played')
plt.show()

# Calculating weighted average of assists and dribbles per match for each club and player
attacking['WeightedAvg'] = ( attacking['assists'] + attacking['dribbles']) / attacking['match_played']
print(attacking['WeightedAvg'])
# Grouping by club and calculating the mean of the weighted averages for each club
average_scores_by_club = attacking.groupby('club')['WeightedAvg'].sum()

# Displaying the calculated averages
print("\nAverage Weighted Scores by Club:")
print(average_scores_by_club)

# Plotting the average scores for each club
plt.figure(figsize=(12, 8))
average_scores_by_club.sort_values(ascending=True).plot(kind='barh', color='skyblue')
#plt.title('Average Weighted Scores of Assists and Dribbles by Football Club')
plt.title('Average Assists and Dribbles per game for Each Football Club')
plt.xlabel('Assists and Dribbles per Match')
plt.ylabel('Football Club')
plt.tight_layout()
plt.show()

df=(average_scores_by_club)
df.to_csv('assists_dribble_game.csv', index=True)