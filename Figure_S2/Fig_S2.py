# Install required libraries by running the command below in the
# terminal (without the #).

# pip install seaborn

# Import libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Table S2, as a .csv file, into a pandas DataFrame. Note that the 
# third row from the table is assigned as the header of the DataFrame.
file1 = "Table_S2.csv"
df = pd.read_csv(file1, header=2)

# Draw the full plot.
p1 = sns.kdeplot(df['KWT'], shade=True, color="r", label="KWT", linewidth=1.5)
p2 = sns.kdeplot(df['AFR'], shade=True, color="b", label="AFR", linewidth=1.5)
p3 = sns.kdeplot(df['AMR'], shade=True, color="g", label="AMR", linewidth=1.5)
p4 = sns.kdeplot(df['EAS'], shade=True, color="y", label="EAS", linewidth=1.5)
p5 = sns.kdeplot(df['EUR'], shade=True, color="m", label="EUR", linewidth=1.5)
p6 = sns.kdeplot(df['SAS'], shade=True, color="c", label="SAS", linewidth=1.5)
plt.axes().spines['top'].set_visible(False)
plt.axes().spines['right'].set_visible(False)
plt.xlim(0, 1)
plt.xlabel("Allele Frequency")
plt.ylabel("Density")
plt.legend(loc='upper left')

# Save plots as figure.
plt.savefig("Output.png", dpi=600)
