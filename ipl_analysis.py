import pandas as pd

df=pd.read_csv("data.csv")
print(df.head())
print("\nColumns:\n",df.columns)
print("\nshape:\n",df.shape)

print("\nTop Winniong teams:\n")
print(df["winner"].value_counts().head(10))

print("\n Top Player of the match:\n")
print(df["player_of_match"].value_counts().head(10))

print("\n Toss Decision Counts:\n")
print(df["toss_decision"].value_counts())

print("\n Matches per city:\n")
print(df["city"].value_counts().head(10))

top_team=df["winner"].value_counts().idxmax()
print("\nTeam with most wins:\n",top_team)

import matplotlib.pyplot as plt

df["winner"].value_counts().head().plot(kind="bar")
plt.title("top 5 winning teams in IPL")
plt.ylabel("No of wins")
plt.xticks(rotation=45)
plt.show()


