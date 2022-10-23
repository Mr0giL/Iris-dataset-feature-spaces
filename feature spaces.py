# import needed libraries
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mtp
###############################################
df = pd.read_csv('iris_csv.csv') #load the Iris dataset
###############################################
# export image of each feature space scatter plot

res1 = sb.scatterplot(data=df,x='petallength',y='petalwidth',hue='class') # create a scatterplot of the selected feature space
out1 = res1.get_figure() # make it as a picture
out1.savefig('p-length to p-width.png') # save that picture

# res2 = sb.scatterplot(data=df,x='petallength',y='sepalwidth',hue='class')
# out2 = res2.get_figure()
# out2.savefig('p-lengh to s-width.png')

# res3 = sb.scatterplot(data=df,x='petallength',y='sepallength',hue='class')
# out3 = res3.get_figure()
# out3.savefig('p-length to s-length.png')

# res4 = sb.scatterplot(data=df,x='petalwidth',y='sepalwidth',hue='class')
# out4 = res4.get_figure()
# out4.savefig('p-width to s-width.png')

# res5 = sb.scatterplot(data=df,x='petalwidth',y='sepallength',hue='class')
# out5 = res5.get_figure()
# out5.savefig('p-width to s-lengh.png')

# res6 = sb.scatterplot(data=df,x='sepallength',y='sepalwidth',hue='class')
# out6 = res6.get_figure()
# out6.savefig('s-width to s-lengh.png')


