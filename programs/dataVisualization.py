import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks",color_codes = True)

Titanic_dataSet = sns.load_data("titanic")
# print(Titanic_dataSet)

p = sns.countplot(x= "sex", hue= "class", data=Titanic_dataSet)
plt.show()