# Install required libraries by running the command below in the
# terminal (without the #).

# pip install seaborn

# Import required libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrane. KWTTopRegionHaps.csv is a
# list of the seven-SNPs (under selection in the TNKS gene region)
# haplotypes habored by the KWT individuals. A digit 1 denotes the
# alternate allele, while the digit 0 means the presence of the
# reference allele.
file1 = "KWTTopRegionHaps.csv"
df = pd.read_csv(file1)

# Set to discriminate the KWT subpopulations in the final plot.
subpop = df.pop("Subpops")

# Draw the full plot.
lut = dict(zip(subpop.unique(), ["red", "whitesmoke", "green"]))
row_colors = subpop.map(lut)
hm = sns.clustermap(df, yticklabels=False, col_cluster=False,
                    standard_scale=1, row_colors=row_colors,
                    cmap=["lightgray", "black"])
hm.cax.set_visible(False)
hm.ax_row_dendrogram.set_visible(False)
plt.setp(hm.ax_heatmap.xaxis.get_majorticklabels(), rotation=0)

# Save plots as figure.
plt.savefig("Output.png", dpi=600)

# The output/image was further modified using an image editor (mainly
# for proper labeling).
