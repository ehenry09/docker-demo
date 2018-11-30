import seaborn as sns
df = sns.load_dataset("iris")
sns_plot = sns.pairplot(df, hue="species")
sns_plot.savefig("my_plot.png")

print("Great Success!")