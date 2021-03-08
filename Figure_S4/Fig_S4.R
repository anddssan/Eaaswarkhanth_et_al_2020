# Install the required package if needed.
install.packages("ggplot2")

# Set working directory to the folder where the two .csv files are 
# located.
setwd("Path:/To/Folder")

# Load required packages.
library("ggplot2")

# Load the .csv files into a dataframe. The correct usage of this script 
# is as follows: 1) Run this script 'as is' to create Output1, i.e., the 
# plot in the left, in Figure S4; and 2) Comment line 17 (adding a # in
# the beginning of the line), and uncomment line 18 (deleting the #) and
# then run the script again in order to create Output2 (the plot in the
# right, in Figure S4).
df <- read.csv("AllTop5Haps.csv", header = TRUE)
# df <- read.csv("KWTTop5Haps.csv", header = TRUE)

# Add labels to the plot legend.
df$Labels <- factor(df$Labels, levels=c("Other","|1001111|","|0111001|",
                                        "|0000000|","|1000000|","|1111111|"))

# Draw the plot.
ggplot(df, aes(fill=Labels, y=Values, x=Pops)) + 
  geom_bar( stat="identity", position="fill") +
  xlab("Populations") + theme(panel.background = element_blank()) +
  ylab("Percentage") + guides(fill=guide_legend(title="Haplotypes", 
                                                reverse = TRUE)) +
  
  # Use whatever colors you like by changing the lines below
  scale_fill_manual(values = c("gray", "violet", "cyan", "green", "yellow", 
                               "red"))

# The outputs/images were further merged and modified using an image
# editor (mainly to enhance readability and to consolidate the legends).
