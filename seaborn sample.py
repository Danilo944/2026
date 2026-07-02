import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('penguins')
sns.pairplot(df, hue='species')

# Save the plot
plt.savefig('penguin.png')