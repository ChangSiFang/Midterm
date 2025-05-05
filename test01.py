import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
df = pd.read_csv('results_01.csv')

# Set plot style
sns.set(style="whitegrid")

# Create the bar plot
plt.figure(figsize=(8,6))
sns.barplot(data=df, x='prompt', y='acc', hue='type')

# Set title and labels
plt.title('Phi-4-q4')
plt.ylabel('acc')
plt.xlabel('prompt')
plt.legend(title='type')

# Save to file
plt.tight_layout()
plt.savefig('test01_results_01.png')
plt.show()
