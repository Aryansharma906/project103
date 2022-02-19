import pandas as pd
import plotly.express as px

dataFrame = pd.read_csv("data.csv")
fig = px.line(dataFrame, x ="date", y ="cases", color ="country" )
fig.show()
