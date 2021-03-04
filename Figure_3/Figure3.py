# Install required libraries by running the command below in the
# terminal (without the #).

# pip install seaborn

# Import libraries.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame. The dataset used here is a
# subset of Tablet S1, in the form of the mainRegion.csv file. It
# contains the values that resulted from all the selection tests, but
# only on for the 86 SNPs located around the TNKS gene (specifically,
# Chr 8: 9300000-9700000, GRCh37/hg19).
file1 = "mainRegion.csv"
df = pd.read_csv(file1)

# Assign data to variables representing x- and y-axis.
x = df["POS"]
y1 = df["iHS"]
y2 = df["XP-EHH KWT vs CEU"]
y3 = df["XP-EHH KWT vs YRI"]
y4 = df["XP-EHH KWT vs CHB"]
y5 = df["PBS KWT vs CEU"]
y6 = df["PBS KWT vs YRI"]
y7 = df["PBS KWT vs CHB"]
y8 = df["LLRS"]

# Draw the full plot.
plt.figure(figsize=(16, 6))

# PLEASE NOTE: Apparently, Seaborn can only draw three plots at a time,
# on a vertical manner. Therefore, the code in lines 44-93 will draw the
# first three Line Plots in the figure (iHS, XP-EHH and PBS results).
# While the (commented) code in lines 96-110 will draw the last Line
# Plot (LLRS results). Thus, the correct usage of this script is as
# followd: 1) Run this script 'as is' to create Output1.png with the
# first three Line Plots; and 2) Comment the lines 44-93, uncomment
# lines 96-110 (deleting the """ in lines 94 and 111) and then run the
# script again in order to create Output2.png with the last Line Plot.

# iHS Line Plot.
ax1 = plt.subplot(3, 1, 1)
plt.plot(x, y1, linewidth=3, color='firebrick', label="KWT")
plt.setp(ax1.get_xticklabels(), fontsize=6)
plt.hlines(2, 9300000, 9700000, linestyles='dashed',
           color='k', label='Threshold')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
plt.tick_params(axis='x', which='both', bottom=False,
                top=False, labelbottom=False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.set_xticklabels([])

# XP-EHH Line Plot sharing the x-axis.
ax2 = plt.subplot(3, 1, 2, sharex=ax1)
plt.plot(x, y2, linewidth=3, color='firebrick', label='KWT vs CEU')
plt.plot(x, y3, linewidth=3, color='forestgreen', label='KWT vs YRI')
plt.plot(x, y4, linewidth=3, color='b', label='KWT vs CHB')
plt.hlines(0, 9300000, 9700000, linestyles='dashed',
           color='k', label='Threshold')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
# Make the tick labels invisible.
plt.setp(ax2.get_xticklabels(), visible=False)
plt.tick_params(axis='x', which='both', bottom=False,
                top=False, labelbottom=False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.set_xticklabels([])

# PBS Line Plot sharing the x-axis.
ax3 = plt.subplot(3, 1, 3, sharex=ax1)
plt.plot(x, y5, linewidth=3, color='firebrick', label='KWT vs CEU')
plt.plot(x, y6, linewidth=3, color='forestgreen', label='KWT vs YRI/CHB')
plt.plot(x, y7, linewidth=3, color='b',
         linestyle='dotted', label='KWT vs YRI/CHB')
plt.hlines(0, 9300000, 9700000, linestyles='dashed',
           color='k', label='Threshold')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
# Make the tick labels invisible.
plt.setp(ax3.get_xticklabels(), visible=False)
plt.tick_params(axis='x', which='both', bottom=False,
                top=False, labelbottom=False)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.set_xticklabels([])

# Save plots as figure.
plt.savefig("Output1.png", dpi=600)
"""
# LLRS Line Plot.
ax1 = plt.subplot(3, 1, 1)
plt.plot(x, y8, linewidth=3, color='r', label="KWT")
plt.setp(ax1.get_xticklabels(), fontsize=6)
plt.hlines(0, 9300000, 9700000, linestyles='dashed',
           color='k', label='Threshold')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
plt.tick_params(axis='x', which='both', bottom=False,
                top=False, labelbottom=False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.set_xticklabels([])

# Save plot as figure.
plt.savefig("Output2.png", dpi=600)
"""
# The outputs/images were further merged and modified using an image
# editor (mainly for proper labeling, highlighting of the main SNPs
# under selection and addition of the TNKS gene model).
