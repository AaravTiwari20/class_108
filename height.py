import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("heightorweight.csv")

fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = False)

fig.show()



