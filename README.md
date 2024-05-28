# Champions-League-Data-Analysis

 Stats of UEFA Champions League 21/22 and the winning possibilities.










































## Introduction:

The UEFA Champions League, often referred to simply as the Champions League, stands as one of the most prestigious and thrilling club football competitions worldwide. Established in 1955, this annual tournament brings together elite clubs from European football associations, showcasing the pinnacle of skill, strategy, and passion on the pitch. With its rich history, intense rivalries, and unforgettable moments, the Champions League captivates millions of fans globally, uniting them in anticipation and excitement as they witness their favorite teams vie for glory on the grandest stage of European football.
The spots are on the players and each player gives a performance that affects his team and increases the chances of winning or reduces it, it is noticeable that we see players with a great performance in the same team but not gaining the games while others with descent players could have a great chance of winning, the proper perspective is that the criteria of a winning club is mixture of high and middle level of players and the important point is that they give together a result which means there’s a chemical reaction between them.
To study this opinion which many experts in the field adopt, we could get datasets that contain all football players who participated in the UCL season 2021/2022, and this data includes many features of the players as pass accuracy, total assists,.. etc.
Moreover, to have clear data on each club we needed first to filter the original data of the players and classify it then find at the end each team's overall score.
This overall data at the end will clarify and it could be used in the future as a measurement to predict the future winners of the next versions of the Champions League.
     
Literature Review and Gaps:
The UEFA Champions League has been an influential event in the world over the past 69 years, with football (soccer) clubs from Europe that have the best players from all around the world hoping to fight for the championship. And of course, as most of the best players in the world are in the league this makes the researchers interested in analyzing the League. For example, Magni, M. et al. (2023) have tried to figure out the evolution of the technique performance from the league. Moreover, game-winning prediction is also something people are interested in, whether football fans, gamblers, or researchers. For example, Hassan, A. et al. (2020) have researched the winning percentages and losses predictions, they also researched the training error of the model. They also add, recently predicted wins and losses, and finding the contribution have been very popular. 



## Abstract 

The UEFA Champions League, originally known as the European Cup and, at times, referred to by the acronyms UCL or UEFA CL, is an annual club association football competition organised by the Union of European Football Associations (UEFA) and contested by top-division European clubs.
This is a research study focusing on predicting the potential winners of the 2020-2021 UEFA Champions League tournament by analyzing detailed statistics of the players. Comprehensive data to assess different aspects of player performance including attack, defense, distribution, and goalkeeping were obtained from Kaggle. They designed a numeric system based on which it is possible to rank the skills of every player participating and predict the possible success of his team. By this system, it simplifies and elaborates on the calculation of the potential result for each team. First, the data was ensured to be complete and unique. The team then prepared the data and came out with a new way to evaluate, in a quantitative fashion, the overall skill levels of the teams. This way, ground prediction could be made of which club might win the championship. Contribution of the research lies not only in improved understanding of what could have made the team successful in one of the top football tournaments but it also sets up a model that can be used for predicting future sports events. The study underscores how crucial, in some games, both individual talent and teamwork play in winning competitive games.


## Contents
-	Intro 
-	Literature review
-	Method
-	Analysis 
-	Final Score
-	Model
-	Summary 
-	Reference (Harvard)
-	Appendices 











## Methodology 
Data Review:	The data of the UCL championship in 2020 - 2021 statistics is obtained from Kaggle. The project mainly aims to predict the winning team in the competition. To do that, we use the data from the database for example on target, attacking, defending, distribution, and the goalkeeping of players in different teams to make our prediction. 

Data Checking: We have checked through the data, and there is no missing data or data duplicates. 

## Data Preparation: 
As the subset of the database such as attacking, defending and distribution contains a large data, we have decided to develop a calculation to reduce columns to make it easier to calculate the average of the overall skills of different teams' players as perspectives to calculate the winner of the UCL championship in 2020 - 2021.

Moreover, in the database, we have the many statistics of each player in the UCL league, however, there is a challenge, it is because although the database gives clear statistics that contribute a lot to the project, it doesn’t have an intuitive visible number to represent each players’ ability, but as we need to calculate the possibility of each club bringing the title of the UCL league, so a visible number is important. Therefore, a calculation is developed for this purpose. 

### Defending Score preparation:
The defending statistic is separated into 3 parts, ball recovery, tackle, and clearance, 3 of the variables are presented in frequency, so we compared with the sum of that category to calculate the score. Since tackle could stop the attack of the other team and make it easier to take control of the ball, we decided to make it the priority, it is worth 40% of the whole ability to defend in the calculation, and ball recovery and clearance will be set at 30% in representing the ability to defends. (tackle*0.4 + ball recovery *0.3 + clearance *0.3) 

Goalkeeping Score preparation: 
The goalkeeping statistic is separated into 4 parts, which are shots saved, penalties saved, a clean sheet, and punch made. However, as for penalties saved, clean sheets, and punches made, these data are present as a frequency, and it is not able to calculate the successful rate for these categories. Therefore, we decided to compare the frequency of a single player with the sum of all players' frequency in that particular category, to make it fair. For the calculation of the score, as saved penalties are a hard technique, therefore it is our priority in the calculation and separate 40% of the whole calculation. In terms of shot saving, is a skill that affects how the whole game is going, so it is in the second priority with 30% in the calculation. In terms of clean sheets, although it represents that the goalkeeper keeps no goals from the opponent, it does not directly represent the goalkeeper's ability so it only separates 20%. And last, for punches made, it is considered one of the techniques to save goals, it does not present the goalkeeper's ability, so it only separates 10%.(shots saved*0.3+ penalties saved*0.4 + clean sheets*0.2 +punches made*0.1)
Distribution Score preparation: (Mohamed):
The distribution dataset is a table that contains all players who participated in the UCL 21/22 and their statistics, for our study there are two important columns: Pass Accuracy and Cross Accuracy which play important roles in the game and could decide the winning of a team, and for data simplification, it was token Pass Accuracy and Cross Accuracy into one column using the next formula: y=0.6*(Pass Accuracy) +0.4(Cross Accuracy), Passing Accuracy was giving a higher coefficient because according to England football website passing plays a more important role. Then, the data was filtered into four categories Defender, Midfielder, Forward, Goalkeeper. Then it was filtered again into each team from the 32 participants and the mean value for each category as it shown in the next table:
Team	Goal Keepers Mean	Defenders Mean	Midfielders Mean	Attackers Mean
Slazburg	44	46	48	53
Wolfsburg	40	47	59	46

### Average on target per game for each team: :
Based on a table which contains data about each player and how many on target he achieved (on target means shooting on the opposite goal frame) we process the data by first make in it into categories (each player in his team category) then by summing up and having the total on target for each team then using other simple dataset which contains each team and how many games it played we could have at the end a table contains the team name and the Mean Value of on target for this team by simply dividing the total per match played as it shows in the next formula:
			Mean_Value=Sum(ON_Target)/(Match_Played)
Ending up with table as the next one:
                          Team	                  Mean_Vlaue
                      Real Madrid	                          5.3
                         Liverpool	                          5.7






### Attacking average for each team 
1.	Load the data: At first, I read the data saved in the CSV file: attacking.csv which is stored in the attacking Pandas DataFrame. This step is important in getting access to the data in the Python platform to be manipulated and used in calculations.
2.	Statistical Summary: By using attacking.describe() I have printed a statistical summary of this data including the count, and mean. The std, min, and max are automatically calculated as well as percentiles are reported for all numeric columns. Also, using agg() I got more specific statistics of the mean, and sum values for the assists, dribbles, and the total for the column that the function is applied on for corner_taken.
3.	Check for missing values: I have confirmed if there are missing values in the DataFrame by attacking.isnull().sum() function.
4.	Data Visualization:
5.	Histograms: I plotted histograms for all numeric features for the distribution of each feature attacking.hist()
6.	Box plots: to get an overall idea and identify the outliers of the distribution of assists, dribbles, or corner_taken you have drawn the box plots.
7.	Scatter Plot with Regression Line: scatterplot with a regression line for assists vs. match_played, as it can show the trend or bias in the representation plotting in a single dot in the scatter plot.
8.	Weighted average: I have introduced a weighted average to manage the performance level of the people based on both the number of assists and dribbles per match and give the assists a high priority of 70% and 30% for the dribbles. Since it shows more how he is engaged with the team and influences the team's performance. And I have calculated Weighted Avg = (0.7 × assists + 0.3 × dribbles)/match_played for each record.
9.	Grouping and average by club: after that, I grouped the data by the club columns calculated the mean for the weighted average scores, and stored it in average_scores_by_club.
10.	Plot Club Performance: Finally, I have plotted these average scores horizontally for each club in the horizontal bar chart by the club to show the club performance visually based on two indicators depicts of club strengths and struggles are ready to use and compare.
### Distrubition average for players
## Loading the Data:
It reads the data from a CSV file into a Pandas DataFrame to allow easy manipulation of the dataset.
Univariate analysis was
Basic Statistics
With the help of the describe() function, it is possible to receive a summary on all numeric columns that are present in the DataFrame: count, mean, std, min, and max.
Detailed Statistics: The statistics for assists and dribbles were specifically calculated using the agg() method. To bring out the summary, we computed the minimum, maximum, mean, standard deviation, and sum of corners.
Handling Missing Values
There was no missing value in the data frame. Removing missing values in this case is important. This is because it could give rise to an error in computation and display imprecision.
Histograms: The following histograms examine the distribution of assists and dribbles.
Boxplots: First, I have plotted the boxplots of assists to check the reason for these peaks, followed by dribbles and corners taken.
Scatter Plot with Regression Line
Assist vs. Matches Played: A scatter plot for the number of assists and matches played is plotted in the following diagram with a regression line in the best possible way to explain the relationship.
Weighted Average Calculation:
Aggregation by Club: The performance data was summarized through the club name to express the mean metrics for each club.
Visualizing Club Performance. The mean values of the weighted metrics for each club were visualized using a horizontal bar chart, hence easy comparison of the values of clubs and which teams generally perform better than others.


 




### Overall Score of each team :
After getting all data needed of all 32 footbal club participated in the UCL we could generate a final table (Data Frame) which contains all features of all teams using Pandas library methods and by make it first in alphabetic order of club’s names to not mismatch data of clubs and then scale the data which needs to be scaled as On Target per game and Assists plus Dribbles per game additionally to Performance of Defenders and Scorekeeping which was not out of 100 using the next scaling formula to make it between [0, 100]:

X(scaled)=[(X-Min(x))/(Max(x)-Min(x))]*(100)+0
Then adding a col of Overall which was calculated as the following:
Overall=0.05*gk_performance+0.1*Scorekeeping+0.05*defenders_performance+0.1*perforamnce_defenders+0.15*attack_performance+0.15*mid_performance+0.2*on_target+0.2*assists_dribble
Why this way of choosing Coefficient:
Coef was distribute equally between position (goal keeper, defenders,...) by 15% where for defenders we divided it 5% for criteria which is more for attacking purpose (Pass_accuracy, cross_accuracy) same for goalkeeper and 10% for actual needed for defenders (tackle won,...) and same for goal keepers. Then we gave on_target 20% and same potion for Assist plus dribble for their important role played in the game.
At the end get a table (Data Frame) which is sorted according to the Overall score (Final Score):

| Club                 |   Overall |
|----------------------|-----------|
| ['Real Madrid']      |     69.01 |
| ['Man. City']        |     61.71 |
| ['Liverpool']        |     58.2  |




## Data Presentation:
Goalkeeping rating of each team in UCL:
For the goalkeeping rating, we have the average score of goalkeeping and football clubs as the variables. As shown in the graph and the table, we can see Real Madrid’s goalkeepers get a score of 39.33 which is the best score in the table, it is 3.81 more than the second place Benfica’s goalkeepers with 35.52. In the third, we got a score of 32.37 for Juventus. 


Clubs	Rating or Score
Real Madrid	39.33
Benfica	35.52
Juventus	32.37
Milan	32.11
Paris	32.08
Dynamo Kyiv	31.25
Villarreal	30.72
Batern	30.71
Malmö	30.44
Sevilla	30.14
 							



Defending rating of each team in UCL:
For the defensive rating, we got the average defensive rating of each football club’s players and the football clubs as the variables. As shown in the table below, Wolfsburg FC seems to have had a great defensive season in UCL with a score of 24.32 as the best score, Beşiktaş FC just behind with a score of 22.45. And at the third, we got Manchester United FC in the third with a score of 21.75.
Clubs	Rating or Score
Wolfsburg	24.32
Beşiktaş	22.45
Man. United	21.75
LOSC	20.58
Leipzig	20.50
Atalanta	20.44
Inter	20.03
Juventus	19.83
Benfica	19.40
Milan	19.24
 



### Attackers and Defenders distribution in each team: 
To present the data, we will first explain the variables. In this case, we have Attackers and Defenders included, we group both attackers and defenders of each team on how well their distribution skills are, which makes our x-axis. On the Y-axis, we have the value calculated with the calculation in the data preparation. As shown in the graph and table, LOSC attackers have performed best skills in distribution with 64 values as the score in the season. Sevillia and Chelsea attackers performed in second and third place with a similar score of 64 and 63 respectively.       
Teams	Score_attacking
LOSC	64
Sevillia	64
Chelsea	63
Ajax	61
Man United	58
Milan	57
Real Madrid	57
Barcelona	57
Bayer	57
Atlético	56
 



## Analysis:
The Attacking and Defending Sorted in both ways and Compared between Teams:

  

The next two bar charts represent the distribution of Attack and Defense for each team where the upper side represents the attack and the lower part represents the defense the difference between the two is that the left one describes it in a sorted way according to attacking values and the left one represent it in the sorted way according to defenders. From those two graphs, we notice that some teams like LOSC (Lille Olympique Sporting Club) have a great attack but weak defense so they didn’t reach above the 16th round and other teams with just above the average attack and defense could go further in the competition as Real Madrid so we could conclude that having a reasonable quality of players in attack and defense plays a significant role better than having a great attack and weak defense. (editable)



















#### The relationship between the defending rating and the goalkeeping rating
  
Table 1: Average goalkeeping score of each FC			Table 2: Average defensive score of each FC

As shown in the graphs above, in Table 1, although some teams have good goalkeeping, they have bad defending. For example, Real Madrid has the highest score in goalkeeping rating, however, their defensive rating shows they are only in the 15th place. This might prove that every team is in a different playing system. For example, some teams’ defence is more reliant on their guards to tackle and interfere with the opponents, but some teams rely more on their goalkeepers’ ability. 


Average On Target per Game for each FC
 

### Analysis: 
The bar chart represents the Mean value of on target per game for all teams (On target means shooting the ball in the goal frame either scoring or not) and we notice that there’s a significant difference between teams, surprisingly Ajax got the most average on target per game even though they did not go further than the 16th round and this was justified according to UEFA.com (2022).
 Their good performance in the group stage(continue)

### Average Assists and Dribbles per game of each FC
 

Top Performers: It features the clubs from the three groups of the top performers. The leading, most probably Bayern, will bring in the highest averages of assists and dribbles per game. This hints at an active and inventive style, resulting in a positive impact on ball possession and goal-scoring opportunities. Other top clubs like Liverpool, Manchester City, and Real Madrid also post high values, with the third club in the list also within the top bracket for possession and scoring attempts.
Middle Bracket Clubs - Clubs that belong to this level: Milan, Paris (most likely Paris Saint-Germain), and Leipzig. They possess average values in both assists and dribbles, which makes them play a kind of balanced game in which creativity is combined with other different genres of tactics.
Top Bracket Clubs: This category also includes Milan, Paris, and Leipzig, which implies they balance creative playing with tactical strategies and maintain average values in assists and dribbles.
Lower Bracket – This category would have the likes of Barcelona, Wolfsburg, and Dynamo Kyiv among the teams. They belong to the lowest average both in assists and dribbles. One may attribute this to the fact that either they possess the ball less or produce fewer dangerous goal-scoring opportunities.
Final score
 
The graph shows all teams that participated in UCL 21/22 ranked from the highest to the lowest score. It shows a lot of interesting information, firstly and by comparing the graph result rank and the actual rank of teams we found 5 out of the top 8 in the graph came in the top 8 of the competition, and the top 3 teams in the UCL are top 3 in the graph and the winner of that version Real Madrid is in the first position of the graph, and this latter tell us about how important is the features discussed above and the impact it may has on the result of the team. Also, we notice there are exceptions for some teams who made it to the 8th round as Atlético Madrid and Benfica which shows that having a medium level of players is not an obstacle to achieving a superior result and also at the same time having a high level of players as Juventus and Paris doesn’t give you directly the winning card.

Model To Predict number of Wins:
After getting the final data we decided to go further by taking number of wins from different data and build a model to predict a team X with its features the number of wins potentially be achieved in UCL tournament and due to the lack of data we have which consist of only 32 teams and one season which is considered a very small data to make a model on it.So after doing some analysis and notice the correlation between features and number of wins we reduced the features into only 3 and this lead to just a fine MSE (Mean Square Error) which mse= 2 where Standard Deviation is approx 20 for each feature, the MSE was calculated based on the test data which is approx 21%. 
Note: The model was build using Linear Regression with the library SkitLearn.



## Summary: 
In this project, we have researched and drafted the dataset of UCL 21/22. 

Rating Calculation and Presentation: 
In this category, we use the datasets’s data to calculate the rating of aspects shown: 
Defending: 
In defending, we projected a calculation with tackle, ball recovery, and clearance. 
As a result, we got Wolfsburg,  Beşiktaş, and Man. United is our top 3 defending teams with our calculation respectively. 
Attacking:
In attack, we use ‘assist’ and ‘Dibble’ as our attributes and calculate the average assist plus dibble in each game of every team. As a result, Bayern, Liverpool, and Man. City is the top 3 in the list.
Goalkeeping:
In Goalkeeping, we projected the calculation with shots saved, penalties saved, clean sheets, and punches made. As a result, we got Real Madrid, Benfica Juventus as our top 3 defending teams with our calculation respectively. 

## Final Score and the model from finding the coefficient:
For the Final Score (overall rating), we have developed a calculation to calculate it which is the graph shown above. In our overall rating, Real Madrid FC got the best rating out of all the teams we got, with a score of 69.01. In the first runner-up, we got Manchester City with a score of 61.71. In the second runner-up, we got Liverpool with a score of 58.2. And in the top 8 of our rating, 5 of the clubs are really in the top 8 in the 21/22 season of UCL, and the top 3 of our rating is also in the top 3 in the 21/22 season of UCL, which could be seen our rating system having quite high accuracy. 

For the model, we use the UCL 21/22 season how many wins each team has and our rating of attacking, defending and goalkeeping, and then try to find out the best coefficient that could actually calculate how many wins each teams have with their rating of attacking defending and goalkeeping. 

## Discussion
As seen in the graphs we have mentioned, we could notice that some of the football clubs have a big difference on defensive rating and goalkeeping rating, or some clubs have a really low assist and dribble per game, for example 1 or lower. These situations are controversial, because in UCL there are 6 games in the group competing round, it is really hard to have that less data to make up the graphs. And apart from that, it’s remarkable that teams with great partly performance  their Overall Score or their achievement is much lower where teams with a good enough in all criteria have a more chance to last to the last rounds, and based on this theory we build a regression model which predict the number of wins based on features which we saw there’s a remarkable correlation.


## Reference:
Magni, M. et al. (2023) Technical differences over the course of the match: An analysis of three elite teams in the UEFA Champions League, MDPI. Available at: https://www.mdpi.com/2075-4663/11/2/46  
me:file:///C:/Users/i7%2011Th/Downloads/SSRN-id3978932.pdf

Hassan, A. et al. (2020) Predicting wins, losses and attributes’ sensitivities in the Soccer World Cup 2018 using neural network analysis, MDPI. Available at: https://www.mdpi.com/1424-8220/20/11/3213  
UEFA.com (2022). Champions League group stage recap: Ajax dazzle all comers | UEFA Champions League. [online] UEFA.com. Available at: https://www.uefa.com/uefachampionsleague/news/0271-14490f5ef067-0bf9d45bda0d-1000--champions-league-group-stage-recap-ajax-dazzle-all-comers/

Association, T.F. (n.d.). What is passing in football? https://learn.englandfootball.com. Available at: https://learn.englandfootball.com/articles-and-resources/coaching/resources/2022/What-is-passing-in-football.


