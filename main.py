import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("studentLevel.csv")
avg_rating_list=df["Avg Rating"].to_list()

fig=ff.create_distplot([avg_rating_list],['average rating of mobile'],show_hist=False)
fig.show()
